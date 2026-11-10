# AP పుస్తకాల లింకులు — app integration

1. Source: `books/AP_Textbook_Links_2026-27_Telugu-English.md`. యూజర్ ఇచ్చిన 66 URLs/మూల పేర్లను మార్చలేదు. Friendly Telugu titles మూల పేర్ల ఆధారంగా మాత్రమే తయారు చేశాం; PDF విషయాలు, medium, edition, remote availability ఇంకా ధృవీకరించలేదు.
2. `index.html`లో APBOOKS markers మధ్య catalog data ఉంటుంది. `V.library`లో **పుస్తకాలు → తరగతి → AP పుస్తకాల లింకులు — 2026–2027** భాగంలో కనిపిస్తుంది. అదే పేజీలో existing local PDFs, teacher-added books వేరు భాగంలో అలాగే ఉన్నాయి.
3. CSE download endpointsకు `.pdf` extension లేదు; cross-origin PDF viewer/CORSపై ఆధారపడకుండా source URLను కొత్త ట్యాబ్‌లో `noopener noreferrer`తో తెరుస్తాం. లింకు పనిచేయకపోతే అధికారిక CSE portalకు fallback link ఉంది. ఇంటర్నెట్ అవసరమని, source-label సందేహాలున్నాయని చూపిస్తాం.
4. Inline catalog app shellలో ఉంటుంది; directory request కోసం వేచి ఉండదు. API unavailable అయినా catalog కనిపిస్తుంది. Slow class-7 request తర్వాత class-8ను తప్పుగా overwrite చేయకుండా load token/current class/current DOM guards ఉన్నాయి.
5. `APPV`ను `2026.11.08-1`కు పెంచాం. Service worker logic, icons/manifest, server code, existing PDFs, notes/answers/SSC data మార్చలేదు. Source URLsను bulk fetch/download చేయలేదు.

## Build

Repo root నుంచి:

```bash
python3 tools/book_links/build_links.py --update-index
```

ఇది Python standard libraryతో నడుస్తుంది. Source counts, HTTPS CSE domain, document IDs/grade match, duplicate URLsను validate చేస్తుంది. Source raw titles/URLs అలాగే ఉంటాయి; known Class-3/Class-2 మరియు English workbook/type label సందేహాలకు notes ఉన్నాయి. Generated inline JSON HTML-safeగా escape చేయబడుతుంది. Default generated preview file `/home/ubuntu/book-links-app/ap_catalog.js`; `--output`తో వేరే output ఇవ్వవచ్చు. `--update-index` ఇవ్వకపోతే app code మారదు.

## Tests

```bash
python3 -m unittest discover -s tools/book_links -p 'test_*.py' -v
node tools/book_links/validate_app.cjs
node tools/sa1_2026_27_class7_8/validate.cjs
node tools/sa1_2026_27/validate.cjs
```

Parser/unit tests source counts/order, labels/warnings, invalid/duplicate URLs, reproducibility, HTML-safe escaping, marker-only updateను పరీక్షిస్తాయి. App fixtures అన్ని 10 తరగతులు/66 source URLs, immediate catalog display, offline catalog, safe new-tab opening, local PDF/teacher-book/tool routes, asynchronous class switching, stored server-code preservationను పరీక్షిస్తాయి.

ఇవి local runtime/source checks; live school-server/CSE PDF download tests కావు. Owner PR merge మరియు GitHub Pages deployment తర్వాతే ఈ app change live అవుతుంది; అప్పటి వరకు mainలో మార్పు లేదు.

## 2025–26 లింకులు (గత సంవత్సరం)

`python3 tools/book_links/build_links_2025.py` – `books/AP_CSE_TextBooks_2025-26_Telugu_English.html` (యూజర్ ఇచ్చిన ఫైల్, మార్చకూడదు) లోని BOOKS → `APBOOKS25`. SEM 2 view లో 2026–27 SEM2 లేనప్పుడు, 📚 అన్నీ view లో details భాగంలో కనిపిస్తాయి.
