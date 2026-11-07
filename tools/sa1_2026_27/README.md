# SA1 గణితం మోడల్ పేపర్లు — 2026–27

9వ, 10వ తరగతులకు యూజర్ పంపిన మూడు చొప్పున SA1 మోడల్ పేపర్లు ఈ data batchలో ఉన్నాయి. ప్రతి పేపర్‌లో 33 ప్రధాన ప్రశ్నలు ఉన్నాయి; 29–33లోని రెండు OR ఎంపికలనూ విడిగా లెక్కిస్తే 38 అంశాలు వస్తాయి. ఆరు పేపర్లకు మొత్తం 228 అంశాలు.

PDFల్లో అధికారిక జవాబు కీ లేదు. ప్రశ్నలు మూల పేపర్ల నుంచి తీసుకున్నవి; తెలుగు అనువాదాలు మరియు తెలుగు/English నమూనా సాధనలు AI రూపొందించినవి. సంఖ్యా/బీజగణిత సాధనలను Python/SymPyతో తనిఖీ చేశారు. పరీక్షకు ముందు ఉపాధ్యాయుడు నమూనా జవాబులను పరిశీలించవచ్చు. మూల పేపర్లలో θ/A పరిధి, చెల్లని అదనపు మూలం, k=0 వల్ల ద్విఘాతం కాకపోవడం వంటి సందర్భాలకు అవసరమైన గమనికలు జవాబుల్లో ఉన్నాయి.

## Appలో కనిపించే చోటు

**నేర్చుకో → గణితం → నోట్స్ ఉన్న అన్ని పాఠాలు**లో `SA1 గణితం మోడల్ పేపర్ 1/2/3 (2026–27)` కనిపిస్తాయి. 9వ తరగతికి కొత్త `notes-9.js`, `answers-9.js` ఉన్నాయి. 10వ తరగతి ఉన్న data filesలో కొత్త revision lessons చేర్చబడ్డాయి. పేపర్ బటన్ అసలు PDFను తెరుస్తుంది; జవాబులు existing teacher-controlled answer-lock విధానాన్నే ఉపయోగిస్తాయి.

నోట్స్‌లో non-MCQ ప్రశ్నలు సాధనలతో ఉన్నాయి. పాఠం టెస్ట్‌లో మూల పేపర్ MCQలు ఉపయోగించబడతాయి. ప్రతి పేపర్‌లో మొత్తం 12 MCQలు ఉన్నాయి; duplicates తీసిన తర్వాత 10వ తరగతి పేపర్ 1, 3లో 11 చొప్పున ప్రత్యేక MCQలు ఉన్నాయి. Existing app ఒకసారి గరిష్ఠంగా 10 ప్రశ్నలను ఎంపిక చేస్తుంది. `wb.qz` ఖాళీగా ఉంచడం వల్ల అదే MCQలు workbook test రూపంలో రెండుసార్లు చేర్చబడవు.

10వ తరగతి కొత్త ప్రత్యేక ప్రశ్నలు SSC bankలో కూడా అసలు chapter IDs (`ma1`–`ma14`), అసలు మార్కులతో ఉన్నాయి. Tags `SA1-2627-P<model>-Q<qid>`; ప్రశ్న పాఠ్యంలో కూడా source label ఉంది. ఇవి ప్రభుత్వ SSC బోర్డు మోడల్ పేపర్లు కావు, అందువల్ల existing `MP1/MP2` tags ఉపయోగించలేదు. మూడు graph ప్రశ్నలకు మూల PDF question-and-graph crops ఉన్నాయి. Notes QA renderer చిత్రాలను render చేయదు కాబట్టి అక్కడ మూల PDFలో ప్ర.21 చూడాలని సూచన ఉంది; SSC rendererలో source graph నేరుగా కనిపిస్తుంది.

## Duplicates మరియు పాత data

- 9వ తరగతి: 114 ప్రత్యేక ప్రశ్నలు.
- 10వ తరగతి: 108 కొత్త ప్రత్యేక ప్రశ్నలు; 6 existing-bank duplicates వదిలారు.
- మొత్తం: 222 కొత్త ప్రత్యేక ప్రశ్నలు, 70 MCQలు, 152 non-MCQ ప్రశ్నలు.
- అన్ని 228 మూల అంశాలకు, నకలు ప్రశ్నలకు కూడా, ఆయా PDF పేజీ వద్ద జవాబులు/సాధనలు ఉన్నాయి.
- Existing notes, answers, SSC records మరియు ఇతర subjects/board metadata/schedules మారలేదు.

`duplicate_review.json`లో similar-wording candidatesకు నిర్ణయాలు ఉన్నాయి. Exact normalized text, దగ్గరగా ఉన్న wording మరియు సంఖ్యలు/constraintsను పోల్చారు. ఒకే భావన ఉన్నా వేరు సంఖ్యలు, వేరు నిరూపణ లక్ష్యం లేదా వేరు subparts ఉంటే నకలుగా తీసివేయలేదు. ఇది ఈ import batchకు చేసిన review; పాత bank మొత్తంలో ఉన్న నకళ్ళను తొలగించే audit కాదు. `import_report.json`లో paper-wise counts మరియు source issue notes ఉన్నాయి.

## Data source మరియు పునరుత్పత్తి

`papers/`లో ప్రతి PDFకు ఒక పూర్తి UTF-8 JSON ఉంది. `qid`, PDF `page`, అసలు `marks`, `lesson_id`, ప్రశ్న/జవాబు/సాధనల తెలుగు మరియు English రూపాలు, options, correct index, source notes ఉంటాయి. `books/9/`, `books/10/`లో యూజర్ ఇచ్చిన PDF bytes అలాగే ఉంచబడ్డాయి. `books/10/sa1-2026-27/`లో మూడు source graph crops ఉన్నాయి.

Repo root నుంచి:

```bash
python3 tools/sa1_2026_27/import_data.py
node tools/sa1_2026_27/validate.cjs
```

Importer Python standard libraryతోనే నడుస్తుంది. App code, server code, `index.html`, `sw.js`, `config.json`, manifest, help filesను మార్చదు. మళ్ళీ నడిపినా ఈ batch lessons/SSC items రెండుసార్లు చేరవు. ఇతర study data అలాగే ఉంటుంది.

Existing `tools/ssc10/build_ssc.py`ను తరువాత నడిపితే, అది revision QAలను ఆటోగా 1/2 మార్కులుగా తయారు చేస్తుంది. అందువల్ల SSC rebuild **తర్వాత** పై SA1 importerను మళ్ళీ నడపాలి. Importer ఈ source-labelled ఆటో itemsను తొలగించి, సరైన chapter/అసలు marksతో canonical SA1 recordsను తిరిగి చేర్చుతుంది.

## చేసిన పరీక్షలు

Data JS syntax; అన్ని ప్రశ్న నంబర్లు/OR ఎంపికల coverage; MCQ correct-answer membership; PDF filename/page lookup; notes render మరియు paper-open function fixtures; SSC IDs/source graphs; పాత data deep equality; source PDF byte equality; importer rerun SHA-256 equality పాస్ అయ్యాయి. Tests local runtime fixtures; ఇవి live school-server end-to-end పరీక్షలు కావు.

Mainలో merge లేదా live deployment చేయలేదు. PRను owner పరిశీలించి merge చేసిన తర్వాత GitHub Pages deployment ద్వారా data live అవుతుంది. ఇప్పటికే తెరిచి ఉన్న appలో కొత్త data కోసం refresh చేయాలి.
