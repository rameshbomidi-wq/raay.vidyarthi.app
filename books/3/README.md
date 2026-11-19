# 3వ తరగతి పుస్తకాలు

## సెమిస్టర్-1 (వర్క్‌బుక్స్)
- Class3_Workbook_Languages_Sem1.pdf, Class3_Workbook_Maths_EVS_Sem1.pdf

## సెమిస్టర్-2 (పాఠ్యపుస్తకాలు – యూజర్ పంపిన PDFలు, 110dpi JPEG గా కుదించాను)
| ఫైల్ | విషయం | ముద్రిత పుట |
|---|---|---|
| Class3_Telugu_Textbook_Sem2.pdf | తెలుగు వికాసం-3 సెమ్-2 (56 పుటలు) | PDF − 8 (పాఠం 6 = PDF 9–19, 7 = 20–32, 8 = 33–43, 9 = 44–55, భావనా పటం 56) |
| Class3_English_Textbook_Sem2.pdf | Blossoms-3 Sem-2 (52) | PDF + 48 (Unit 5 = PDF 3–15, 6 = 16–28, 7 = 29–39, 8 = 40–51, Mind map 52) |
| Class3_Maths_Textbook_Sem2_Telugu.pdf | గణితంతో గమ్మత్తు సెమ్-2 – తెలుగు పేజీలు మాత్రమే (76) | 2×PDF − 1 |
| Class3_EVS_Textbook_Sem2_Telugu.pdf | మన అద్భుత ప్రపంచం సెమ్-2 – తెలుగు పేజీలు మాత్రమే (55) | 2×PDF + 151 |

బిల్డ్: `python3 tools/class3/build3.py` (ch/*.py → notes-3.js, answers-3.js; సెమ్-1 పాఠాలు అలాగే).

## సెమ్-2 గణితం వర్క్‌బుక్ (2026-11-19, యూజర్ PDF → 110dpi JPEG)
Class3_Maths_Workbook_Sem2.pdf – 88 పుటలు, PDF = ముద్రిత + 4. ద్విభాషా: చాలా వర్క్‌షీట్లు ఇంగ్లీష్ పేజీ + తెలుగు పేజీ జతలు. 5 భాగహారం PDF 6–27, 6 భిన్నాలు 28–37, 7 దత్తాంశ నిర్వహణ 38–43, 8 జ్యామితి 44–57, 9 కొలతలు 58–85, అపోహల పోస్టర్ 86–88.
జవాబులు: `tools/class3/wb/w<N>.py` (WB, WSEC=[((పేజీలు), శీర్షిక, జవాబులు)]) – build3.py ma<N> పాఠం wb ని వర్క్‌బుక్‌కు మార్చి, పాఠ్యపుస్తకం పరిధిని wb.tb లో ఉంచుతుంది (index.html ansLessonOf wb.tb చూస్తుంది).
