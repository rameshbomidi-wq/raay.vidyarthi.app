#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
import tempfile
import unittest
from pathlib import Path

# Make this file runnable directly as well as through unittest discovery.
HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import build_links


REPO = HERE.parents[1]
SOURCE = REPO / "books/AP_Textbook_Links_2026-27_Telugu-English.md"


class BuildLinksTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.source_text = SOURCE.read_text(encoding="utf-8")
        cls.catalog = build_links.build_catalog(cls.source_text)

    def test_parse_counts_and_source_order_are_preserved(self) -> None:
        grades = build_links.parse_source(self.source_text)
        self.assertEqual({g: len(v) for g, v in grades.items()}, build_links.EXPECTED_COUNTS)
        source_urls = [
            url
            for url in re.findall(r"^\s*\d+\.\s+\[[^\]]+\]\((https?[^\s)]+)\)", self.source_text, re.M)
        ]
        catalog_urls = [row[2] for grade in self.catalog.values() for row in grade]
        self.assertEqual(catalog_urls, source_urls)
        self.assertEqual(len(set(catalog_urls)), 66)

    def test_rows_have_exact_four_fields_and_raw_title(self) -> None:
        self.assertTrue(all(len(row) == 4 for rows in self.catalog.values() for row in rows))
        self.assertEqual(
            self.catalog["1"][0][1],
            "WORK BOOK FOR CLASS 1_SEM1 (Work Book)",
        )
        self.assertEqual(
            self.catalog["1"][0][2],
            "https://cse.ap.gov.in/loadsupdocumentuploadbyid?req_doc_id=2026-2027W01170012609191257520BRF8",
        )

    def test_friendly_labels_use_only_conservative_title_hints(self) -> None:
        # Generic class 1 bundle titles must not be guessed as Telugu.
        self.assertNotIn("తెలుగు", self.catalog["1"][0][0])
        self.assertEqual(self.catalog["1"][0][0], "వర్క్‌బుక్ — SEM1")
        self.assertEqual(self.catalog["6"][1][0], "తెలుగు ద్వితీయ భాష — పాఠ్యపుస్తకం")
        self.assertEqual(self.catalog["6"][3][0], "గణితం — పాఠ్యపుస్తకం — SEM1")
        self.assertEqual(self.catalog["10"][6][0], "భూగోళం — పాఠ్యపుస్తకం")
        self.assertEqual(self.catalog["10"][12][0], "English — ఉపవాచకం — SEM1")
        self.assertEqual(self.catalog["10"][7][0], "భౌతిక శాస్త్రం — పాఠ్యపుస్తకం")
        self.assertEqual(self.catalog["10"][8][0], "జీవశాస్త్రం — పాఠ్యపుస్తకం")

    def test_explicit_ambiguity_warnings(self) -> None:
        self.assertEqual(
            self.catalog["3"][1][3],
            "మూల పేరులో 2వ తరగతి ఉంది; ఇది 3వ తరగతి జాబితాలో ఉంది. PDF చూసి ధృవీకరించండి.",
        )
        self.assertIn("Work Book", self.catalog["9"][5][3])
        self.assertIn("Text Book", self.catalog["9"][5][3])
        self.assertIn("PDF చూసి ధృవీకరించండి", self.catalog["10"][10][3])
        self.assertEqual(self.catalog["10"][11][3], "")

    def test_duplicate_url_is_rejected(self) -> None:
        urls = list(re.finditer(r"https://cse\.ap\.gov\.in/loadsupdocumentuploadbyid\?req_doc_id=[^\s)]+", self.source_text))
        # Duplicate within grade 10 so document-grade validation still passes.
        duplicate_text = self.source_text[: urls[-1].start()] + urls[-2].group(0) + self.source_text[urls[-1].end() :]
        with self.assertRaisesRegex(build_links.LinkBuildError, "duplicate URL"):
            build_links.build_catalog(duplicate_text)

    def test_grade_mismatch_is_rejected(self) -> None:
        old = "req_doc_id=2026-2027W03170012609191259649PKWX"
        new = "req_doc_id=2026-2027W02170012609191259649PKWX"
        with self.assertRaisesRegex(build_links.LinkBuildError, "grade does not match"):
            build_links.build_catalog(self.source_text.replace(old, new, 1))

    def test_rendering_is_reproducible_and_html_safe(self) -> None:
        first = build_links.render_block(self.catalog)
        second = build_links.render_block(build_links.build_catalog(self.source_text))
        self.assertEqual(first, second)
        decoded = json.loads(first.split("const APBOOKS=", 1)[1].split(";\n", 1)[0])
        self.assertEqual(decoded, self.catalog)
        self.assertNotIn("</", first)
        self.assertNotIn("\u2028", first)
        self.assertNotIn("\u2029", first)

    def test_marker_update_changes_only_delimited_block(self) -> None:
        block = build_links.render_block(self.catalog)
        with tempfile.TemporaryDirectory() as directory:
            index = Path(directory) / "index.html"
            before = "<!doctype html>\n<header>keep</header>\n" + build_links.START_MARKER + "\nold\n" + build_links.END_MARKER + "\n<footer>keep</footer>\n"
            index.write_text(before, encoding="utf-8")
            build_links.update_index(index, block)
            after = index.read_text(encoding="utf-8")
            self.assertEqual(
                after,
                "<!doctype html>\n<header>keep</header>\n" + block + "\n<footer>keep</footer>\n",
            )

    def test_marker_update_fails_when_markers_are_absent(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            index = Path(directory) / "index.html"
            index.write_text("<html>no block</html>\n", encoding="utf-8")
            with self.assertRaisesRegex(build_links.LinkBuildError, "markers absent"):
                build_links.update_index(index, build_links.render_block(self.catalog))


if __name__ == "__main__":
    unittest.main()
