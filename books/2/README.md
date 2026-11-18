2వ తరగతి పుస్తకాలు
- Class2_Workbook_Sem1.pdf – వర్క్‌బుక్ సెమిస్టర్-1 (తెలుగు లోగిలి PDF 8–52, English 54–86, గణితం 87–133; PDF పేజీ = ముద్రిత పేజీ + 6)

## సెమిస్టర్-2 పాఠ్యపుస్తకాలు (2026-11-18; యూజర్ పంపిన PDFలు → 110dpi JPEG, img2pdf + qpdf)
| ఫైల్ | పుస్తకం | ముద్రిత పుట |
|---|---|---|
| Class2_Telugu_Textbook_Sem2.pdf | తెలుగు లోగిలి-2 సెమ్-2 (64) | PDF = ముద్రిత (9 చిచ్చుబుడ్డి 1–6, 10 అరటిచెట్టు 7–12, 11 అద్దాల బస్సు 13–18, 12 కొయ్యగుర్రం 19–24, 13 మొక్కజొన్న 25–30, 14 అమ్మమ్మగారిల్లు 31–36, 15 పాపనవ్వు 37–42, 16 ఒత్తులబుట్ట 43–48, 17 మ్యావ్ మ్యావ్ 49–54, 18 కాలచక్రం 55–60, పద్యాలు 61–62, సూక్తులు 63) |
| Class2_English_Textbook_Sem2.pdf | Blossoms-2 Sem-2 (84) | PDF + 64 (3.1 Healthy Foods 5–14, 3.2 Our Friends in Nature 15–25, 4.1 Our Festivals 26–35, 4.2 Ravi's Birthday 36–43, 5.1 My Grandpa's Village 44–54, 5.2 Our Helpers 55–63, 6.1 Our Fair 64–72, 6.2 Wheels on the Bus 73–83, Mind map 84) |
| Class2_Maths_Textbook_Sem2_Telugu.pdf | గణితంతో గమ్మత్తు-2 సెమ్-2 – తెలుగు పేజీలు మాత్రమే (87) | 2×PDF + 147 (అధ్యా. 4 సంఖ్యలతో ఆడుకుందాం 2–20, 5 ఎన్ని రెట్లు? 21–39, 6 పంచుకుందాం 40–49, 7 మనం కొలుద్దాం 50–62, 8 కాలం 63–77, 9 మన చుట్టూ ఉన్న ఆకారాలు 78–87) |
OCR: pdftoppm 200dpi gray + tesseract (తెలుగు/గణితం tel+eng psm 4, tessdata_best; English eng). English pdftotext పనిచేయదు (Identity font) → OCR.
బిల్డ్: `python3 tools/class2/build2.py` (ch/*.py → notes-2.js, answers-2.js; సెమ్-1 పాఠాలు అలాగే).
