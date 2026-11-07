# 7వ, 8వ తరగతి SA1 గణితం — పాయింట్‌వైజ్ సాధనలు

యూజర్ ఇచ్చిన రెండు Solutions PDFలలోని ప్రశ్నలు, ఇచ్చిన సాధనలను పరిశీలించి existing study-data formatలో చేర్చిన batch ఇది. ఒక్కో తరగతికి 33 ప్రధాన ప్రశ్నలు ఉన్నాయి; 30–33లో రెండు OR ఎంపికలనూ వేర్వేరుగా ఉంచడం వల్ల 37 అంశాలు వస్తాయి. రెండు తరగతులకు మొత్తం 74 అంశాలు, 40 మూల MCQలు.

## విద్యార్థికి ఉపయోగపడే జవాబు పద్ధతి

జవాబులు చిన్న నంబర్‌డ్ పాయింట్లుగా ఉన్నాయి. గణితంలో ఇచ్చినవి → అవసరమైన సూత్రం → విలువల ప్రతిక్షేపణ → మధ్య దశలు → యూనిట్లతో తుది జవాబు క్రమం పాటించాం. నిరూపణల్లో ప్రతి ముఖ్య దశకు కారణం ఉంది. 1–2 మార్కులకు అవసరమైన క్లుప్త వివరణ, 4–8 మార్కులకు పూర్తి దశలు ఉన్నాయి. తెలుగు మరియు English steps arrays source JSONలో ఉన్నాయి.

User preferenceను `CLAUDE.md`లో కూడా నమోదు చేశాం, తర్వాతి content పనుల్లో అదే పద్ధతి కొనసాగించడానికి. ఇది documentation మార్పు మాత్రమే; app/server code మార్పు కాదు. పాత 9/10 తరగతి dataను ఈ batch మార్చదు.

## Existing app rendering

`notes-7.js`, `notes-8.js`లో `sa1mp1` revision lesson ఉంది. **నేర్చుకో → గణితం → నోట్స్ ఉన్న అన్ని పాఠాలు → SA1 గణితం మోడల్ పేపర్ 1 — పాయింట్‌వైజ్ సాధనలు (2026–27)**లో చూడవచ్చు.

Existing QA renderer `<p>`లో plain newlinesను చూపించదు. App CSS/code మార్చకుండా, ఇప్పటికే ఉన్న rich-text `fg` data blockలో ప్రతి ప్రశ్నకు పాయింట్‌వైజ్ సాధన కూడా ఇచ్చాం. ఈ భాగానికి appలో ఉన్న parent heading “పటాలు – పట్టికలు”; దాని లోపల “ప్ర. … — పాయింట్‌వైజ్ సాధన” అనే స్పష్టమైన titles ఉన్నాయి. Existing `richT` ద్వారా numbered steps వేర్వేరు లైన్లలో కనిపిస్తాయి. QA entriesలో కూడా అదే numbered solution text భద్రపరచబడింది.

`answers-7.js`, `answers-8.js`లో ప్రతి దశను వేరు array entryగా ఉంచాం; existing PDF answer panelలో అవి వేరు list entriesగా కనిపిస్తాయి. మూల sourceకు question page, answer page వేరు అయితే రెండు పేజీల దగ్గర model steps ఉన్నాయి. Diagram ప్రశ్నలకు self-contained verbal descriptions, source-page references ఇచ్చాం.

**గమనిక:** యూజర్ పంపిన మూల PDFలలో సాధనలు ముద్రించి ఉన్నాయి. Existing answer-lock PDFలో ముద్రించిన జవాబులను దాచదు; అదనపు answer panelకే వర్తిస్తుంది. అసలు PDF bytes మార్చలేదు. Sourceలో ఇచ్చిన సాధనలను పరిశీలించి point-wise రూపంలో మార్చాం; sourceను అధికారిక exam keyగా పేర్కొనలేదు. Source solutionsలో correction అవసరం ఉన్న గణిత తప్పు గుర్తించలేదు.

## Duplicates మరియు quiz

ప్రతి తరగతి లోపల పూర్తి ప్రశ్న/MCQ options ఆధారంగా normalized-text duplicates చూశాం; ఈ batchలో duplicate అంశాలు లేవు. 7వ, 8వ తరగతులు వేర్వేరు curriculum groups కాబట్టి రెండు తరగతుల మధ్య concept overlapను ఒక తరగతిలో తీసివేయలేదు. Import ముందు 7/8 తరగతి notes/answers files లేవు. ఇది పాత app మొత్తంలో semantic duplicate audit కాదు.

మూల 20 MCQల options/సరైన జవాబు ఒక్కో తరగతికి quizలో ఉన్నాయి. కొత్త distractors సృష్టించలేదు. Source option labels మరియు original answer wording JSONలో `source_options_*`, `source_answer_*` రూపంలో ఉన్నాయి; quiz కోసం A/B/C/D label prefixesను తొలగించాం. Existing app ఒకసారి గరిష్ఠంగా 10 ప్రశ్నలను ఎంచుకుంటుంది.

## Rebuild మరియు పరీక్షలు

Repo root నుంచి:

```bash
python3 tools/sa1_2026_27_class7_8/import_data.py
node tools/sa1_2026_27_class7_8/validate.cjs
node tools/sa1_2026_27/validate.cjs
```

Importer Python standard libraryతో నడుస్తుంది. మళ్ళీ నడిపితే ఈ batch data రెండుసార్లు చేరదు; ఇతర notes/answers అలాగే ఉంటాయి. Source JSONలు `papers/`లో, counts/issues `import_report.json`లో ఉన్నాయి.

పాస్ అయిన checks: source question/OR coverage, point-wise steps, MCQ option membership, actual rich-text `<br>` rendering, PDF answer-panel separate entries, paper-open/quiz fixtures, 7/8 data syntax, source PDF byte equality, importer rerun hash equality, పాత 9/10 data tests. `index.html`, `sw.js`, config, manifest, help/server code, అన్ని పాత study data files unchanged. ఇవి local runtime fixtures; live school-server end-to-end tests కాదు.

ఈ branchను mainలో merge చేయలేదు. Owner PRను పరిశీలించి merge చేసిన తర్వాత Pages deployment పూర్తవ్వాలి; అప్పుడే appలో కొత్త data కనిపిస్తుంది. App refresh అవసరం కావచ్చు.
