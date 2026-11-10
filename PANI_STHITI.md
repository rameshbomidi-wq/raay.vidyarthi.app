# పని స్థితి (Claude కోసం – ప్రతి commit తో అప్‌డేట్ చేయాలి)

చివరి అప్‌డేట్: 2026-11-10 • 8వ తరగతి English e01–e09 (పూర్తి); హిందీ h01

## ఇప్పుడు నడుస్తున్న పని
- 8వ తరగతి (build `tools/class8/build8.py`). ✅ గణితం 7, సైన్స్ (phy 5 + bio 3), తెలుగు 7, తెలుగు ద్వితీయ భాష 6 – పూర్తి.
- ⏳ Languages `books/8/Class8_Languages_Textbook_Sem1.pdf` (PDF = ముద్రిత + 8):
  - English Blooming Minds (ch/eNN.py, ids e8u1a…): text = `pdftotext -layout` + decode (encoded tokens chr+29; సాదా పదాలున్న tokens అలాగే) – scratchpad `/home/claude/w8/scripts/en_dec.py`. పరిధులు: U1 (జూలై) a The Wit that Won Hearts 252–268, b A Concrete Example 269–278, c Wisdom Paves the Way 279–297 (Transcripts 298–300); U2 a A Tale of Valour (Major Somnath Sharma) 301–323, b Somebody’s Mother 324–337 (ఆగస్టు), c Verghese Kurien – I Too Had a Dream 338–353 (సెప్టెంబర్) (Transcripts 354–356); U3 a The Case of the Fifth Word 357–378, b The Magic Brush of Dreams 379–393 (సెప్టెంబర్), c Spectacular Wonders 394–409 (అక్టోబర్) (Transcripts 410–412). పూర్తి: e01–e09 (పూర్తి).
  - హిందీ मकरंद (ch/hNN.py, h8lN): OCR `tesseract -l hin+eng --psm 4` 200dpi → `/home/claude/w8/hi/<p>.txt`. 1) सुबह 154–163 2) तेनालीराम की चतुराई 164–173 3) श्रीहरिकोटा 174–186 4) किसान 187–197 5) कूड़ेदान 198–210 6) मित्र को पत्र 211–219 7) गोल 220–231. పూర్తి: h01.
- ⏳ సాంఘికం – PDF ఇంకా రాలేదు (యూజర్ పంపాలి). 

## తర్వాత చేయవలసినవి (క్రమంలో)
1. 7వ తరగతి Languages ✅ పూర్తి (English 9, తెలుగు 6, హిందీ 7 – ch/e01–e09, t01–t06, h01–h07). పుస్తకంతో సరిచూడవలసినవి: హిందీలో “पुस्तक से मिलाइए” గమనిక ఉన్న అంశాలు (బొమ్మల ఆధారిత రిక్త స్థానాలు/पर्याय/बेमेल), తెలుగులో “పుస్తకంతో సరిచూడండి” అంశాలు. చేయనివి: మూడు భాషల సంసిద్ధత (Readiness) భాగాలు.
2. 7వ తరగతి: సాంఘికం ✅, తెలుగు ద్వితీయ భాష ✅ (2026.11.10-7). సరిచూడవలసినవి: సాంఘికం c06 Fig 6.27 చిత్ర క్రమం, c07 ప్ర.11 పటం, c08 కార్టూన్; ద్వితీయ తెలుగు l05 (వచనం మార్పు 2–5, క్రియలు 1, 3), l06 పదజాలం వాక్యాలు.
3. 7వ తరగతి పుస్తకంతో సరిచూడవలసినవి: గణితం పుట 184 (A–D), పుట 310 (ఎత్తుల బొమ్మ), Fig 5.5/5.6, 3.2 ప్ర.1, 6.5 ప్ర.3. English: e05 currant bun బొమ్మ ఎంపిక (PDF 302), e07 poster (PDF 347–348), e09 crossword 12 Across పెట్టెల సంఖ్య.
4. 8వ తరగతి మిగిలినవి: సైన్స్, సాంఘికం, Languages (యూజర్ 2026-11-10 న Languages SEM1 PDF పంపారు – `books/8/Class8_Languages_Textbook_Sem1.pdf` గా repo లో పెట్టాలి), English, తెలుగు ద్వితీయ భాష.
5. 6వ తరగతి సెమ్-2, 1–5 తరగతుల సెమ్-2 – PDFలు వచ్చినప్పుడు.

## మధ్యలో ఆగితే
- ఇక్కడ “ఇప్పుడు నడుస్తున్న పని” లో: తరగతి, సబ్జెక్టు, పూర్తయిన ch ఫైళ్లు, తర్వాతి అధ్యాయం, దాని PDF పేజీ పరిధి రాయాలి.
