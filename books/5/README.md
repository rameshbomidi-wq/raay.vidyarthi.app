# 5వ తరగతి పుస్తకాలు

## సెమిస్టర్-1 (వర్క్‌బుక్స్)
- Class5_Workbook_Languages_Sem1.pdf, Class5_Workbook_Maths_EVS_Sem1.pdf (PDF = ముద్రిత + 6)

## సెమిస్టర్-2 (పాఠ్యపుస్తకాలు – యూజర్ పంపిన PDFలు, 110dpi JPEG గా కుదించాను)
| ఫైల్ | విషయం | ముద్రిత పుట |
|---|---|---|
| Class5_Telugu_Textbook_Sem2.pdf | తెలుగు వికాసం-5 సెమ్-2 (70 పుటలు) | PDF − 10 (పాఠం 6 పెన్నేటి పాట = PDF 11–22, 7 పద్యరత్నాలు = 23–34, 8 ఇటిజ్ పండుగ = 35–46, 9 తరిగొండ వేంగమాంబ = 47–58, 10 మంచి బహుమతి = 59–69, భావనా పటం 70) |
| Class5_English_Textbook_Sem2.pdf | Blossoms-5 Sem-2 (72) | PDF + 60 (Unit 5 = PDF 3–18, 6 = 19–34, 7 = 35–53, 8 = 54–71, Mind map 72) |
| Class5_Maths_Textbook_Sem2_Telugu.pdf | గణితంతో గమ్మత్తు సెమ్-2 – తెలుగు పేజీలు మాత్రమే (98) | 2×PDF − 13 (అధ్యా. 5 = PDF 8–26, 6 = 27–36, 7 = 37–66, 8 = 67–84, 9 = 85–98) |
| Class5_EVS_Textbook_Sem2_English.pdf | Our Wonderful World సెమ్-2 – English పేజీలు మాత్రమే (61) | 2×PDF + 182 (పాఠం 7 = PDF 2–12, 8 = 13–23, 9 = 24–37, 10 = 38–47, 11 = 48–59) |

బిల్డ్: `python3 tools/class5/build5.py` (ch/*.py → notes-5.js, answers-5.js; సెమ్-1 పాఠాలు అలాగే).
OCR: తెలుగు పేజీలు legacy font → `pdftoppm -r 200` + `tesseract --tessdata-dir /home/claude/td/tb -l tel+eng --psm 4` (tessdata_best sparse clone); EVS = tesseract eng; English = pdftotext సాదా.
