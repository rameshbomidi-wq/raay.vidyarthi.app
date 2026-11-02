# రాయ్ విద్యార్థి లెర్నింగ్ యాప్ – పని కొనసాగించడానికి గైడ్ (Claude కోసం)

యజమాని: బోమిడి రమేష్ (SGT, ZPHS TV Palli, గూడూరు మండలం, SPSR నెల్లూరు). తెలుగు/Tenglish లో క్లుప్తంగా, పూర్తిగా చేసి ఇవ్వాలి.
ప్రతి జవాబు చివర: `రాయ్ ఎడ్యుకేషన్ – https://raayeducation.in`

## యాప్
- Single-file PWA: `index.html` (~1.2 MB). Live: https://rameshbomidi-wq.github.io/raay.vidyarthi.app/
- మార్పులు నేరుగా ఈ repo లో commit + push చేయాలి (యూజర్ upload చేయనవసరం లేదు). ప్రతి మార్పుకు `APPV` (index.html లో `const APPV='YYYY.MM.DD-n'`) పెంచాలి.
- `sw.js` – icons/manifest మారితే `VER` పెంచాలి. `notes-*.js` network-first.
- సర్వర్: Google Apps Script (పబ్లిక్ multi-school). కోడ్ index.html లోని `<script type="text/plain" id="ms-code">` లో ఉంటుంది. సర్వర్ మారితే ఆ భాగం నుండి `.gs` ఫైల్ తీసి యూజర్‌కు పంపి
  “⚠️ సర్వర్ కోడ్ మారింది – deploy చేయండి (✏️ → New version, మూడు deployments)” అని చెప్పాలి. మారకపోతే పంపకూడదు.
- సర్వర్ collections: COLS/TCOLS (client `COLS` + `def()` + gs-code + ms-code అన్నిచోట్లా కలపాలి). ping flags: up, roster, qp, pdfs, tbx, ak.
- విద్యార్థుల వ్యక్తిగత డేటా (పేర్లు, DOB) repo/పబ్లిక్ ఫైళ్లలో ఎప్పుడూ పెట్టకూడదు.

## పాఠ్యపుస్తకం కంటెంట్ (ప్రతి తరగతికి ఒకే పద్ధతి – 3వ తరగతి పూర్తి నమూనా)
- `notes-<c>.js` → `(window.RAAY_TB=window.RAAY_TB||{})[c]={tel:[...],eng:[...],mat:[...],evs:[...]}`
  పాఠం: `{id,no,t,m:[నెలలు],ty,th,by,sum,te?(eng),pts[],w:[[పదం,అర్థం]],gr:{t,p[]},qa:[[q,a]],act,kn,qz:[[q,సరైనది,తప్పు1,తప్పు2,తప్పు3]] (≥10; maths లో concept ప్రశ్నలు కూడా – random 10),
  wb:{pg,f:'books/<c>/...pdf',p:(PDF పేజీ),ws[],mis,qz[]}, tg:[[శీర్షిక,[జవాబులు]]]}` (tg = టీచర్ గైడ్: చిత్రం చూడండి, ఇవి చేయండి, Activities, Do these, Exercises)
- `answers-<c>.js` → `(window.RAAY_ANS=...)[c]={'<workbook file>':{'<pdf page>':['— శీర్షిక —','జవాబు',...]}}` – టీచర్ లాక్ తెరిచాకే పిల్లలకు.
- వర్క్‌బుక్ PDFలు: `books/<c>/Class<c>_Workbook_*_Sem<n>.pdf` (`qpdf --linearize`).
- అకాడమిక్ క్యాలెండర్ `ACAL` (1–5) లో తప్పు తెలుగు పాఠం పేర్లను పుస్తకం చూసి సరిచేయాలి.
- PDF text: English/Maths ఫాంట్లు shift cipher (chr+29 లేదా −2) – decode చేయాలి; తెలుగు పేజీలు బొమ్మలుగా చదవాలి.

## పూర్తయినవి
- 3వ తరగతి సెమిస్టర్-1: తెలుగు 5, English 4, గణితం 4, EVS 6 పాఠాలు – notes, పాఠం టెస్ట్, వర్క్‌బుక్ టెస్ట్, వర్క్‌బుక్ జవాబులు, టీచర్ గైడ్.
## తర్వాత
- 3వ తరగతి సెమిస్టర్-2; 1, 2, 4, 5 తరగతులు (యూజర్ PDFలు పంపుతారు).

## పరీక్ష
- `python3 -m http.server` + Playwright (chromium ముందే ఉంది). `node --check` అన్ని `<script>` blocks.
- pdf.js CDN sandbox లో అందదు → `/opt/npm-tools/node_modules/pdfjs-dist/legacy/build/` ని route చేసి పరీక్షించాలి.
- ఫంక్షన్ పేర్లు duplicate కాకుండా చూడాలి (ఇంతకు ముందు `pdfDraw`, `ansLoad`, `ansOpen` clash అయ్యాయి).
