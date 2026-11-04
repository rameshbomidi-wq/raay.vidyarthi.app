# 10వ తరగతి భాషా పాఠాలు – పని కొనసాగించే సాధనాలు

1. పుస్తకాలు `books/10/Class10_Telugu_Textbook_Sem1.pdf` (tel), `Class10_Telugu_SecondLanguage_Textbook.pdf` (te2), `Class10_Hindi_Textbook_Sem1.pdf` (hin) ని పని ఫోల్డర్‌లో `tel.pdf`, `tel2.pdf`, `hin.pdf` గా కాపీ చేయండి.
2. తెలుగు OCR: `tel.traineddata` ను `https://github.com/tesseract-ocr/tessdata_best/raw/main/tel.traineddata` నుండి దించి `ocr.sh` లోని `T=` ఫోల్డర్‌లో పెట్టండి (eng, hin, osd కూడా `/usr/share/tesseract-ocr/5/tessdata/` నుండి కాపీ). `./ocr.sh tel tel+eng`, `./ocr.sh tel2 tel+eng`, `./ocr.sh hin hin+eng` (≈15 ని.).
3. `secmap.sh a b` – పాఠం PDF పేజీల్లో అభ్యాస విభాగాలు ఏ పేజీలో ఉన్నాయో చూపుతుంది; `python3 lx.py a b` – OCR పాఠ్యం.
4. ప్రతి పాఠానికి `ch/tNN.py` (S, PAGES, L, SEC=[(pdf పేజీ, శీర్షిక, [జవాబులు])]) – నమూనా `t01.py`, `t02.py`. హిందీకి `S='hin'`, ద్వితీయ భాషకు `S='te2'`.
5. `python3 build_lang.py` → notes-10.js, answers-10.js లో కలుపుతుంది (మిగిలిన సబ్జెక్టులు అలాగే ఉంటాయి). `REPO`, `H` మార్గాలు సరిచూసుకోండి.

PDF పేజీ = ముద్రిత పేజీ + 8 (తెలుగు రెండు పుస్తకాలు), హిందీ PDF = ముద్రిత + 2.
తెలుగు ప్రథమ భాష పాఠాల PDF పరిధులు: 1: 9–22, 2: 23–34, 3: 35–45, 4: 46–59, 5: 60–72, 6: 73–82, 7: 83–93, 8: 94–107, 9: 108–119, 10: 120–135, 11: 136–145, 12: 146–158 (ఉపవాచకం రామాయణం 159–200).
మాసాలు: 1–2 జూన్, 3–4 జూలై, 5–6 ఆగస్టు, 7–8 సెప్టెంబర్, 9–10 అక్టోబర్, 11–12 నవంబర్.

పాఠం ids: తెలుగు ప్రథమ భాష te1…te12, హిందీ hi1…hi12, ద్వితీయ భాష తెలుగు sl1…slN (te2_ లాంటివి వాడకండి – టెస్ట్ ఫలితాల ids కలిసిపోకూడదు).


స్థితి (2026.11.04-6): tel te1–te12, te2 sl1–sl10, hin hi1–hi12 పూర్తి. OCR: `lx.py` కి `B=tel2` / `B=hin` env ఇవ్వండి; `tel.traineddata` ను raw.githubusercontent.com/tesseract-ocr/tessdata_best/main/tel.traineddata నుండి దించండి.
ద్వితీయ భాష PDF పరిధులు: 1: 9–15, 2: 16–25, 3: 26–32, 4: 33–44, 5: 45–52, 6: 53–66, 7: 67–72, 8: 73–81, 9: 82–91, 10: 92–101.
హిందీ PDF పరిధులు: 1: 10–14, 2: 15–21, 3: 26–30, 4: 34–38, 5: 39–46, 6: 48–54, 7: 61–65, 8: 66–72, 9: 74–78, 10: 81–84, 11: 85–90, 12: 93–100.
