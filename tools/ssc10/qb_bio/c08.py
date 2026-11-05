# 8. అనువంశికత (Heredity) – Marks: 10   |   13. మన పర్యావరణం (Our Environment) – Marks: 10
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from figlib import IMG
I = 'ssc/img/bio/'
MONO = ('మెండెల్ ఏకసంకరణం (పొడవు, పొట్టి బఠాణీ మొక్కలు):\nP తరం: పొడవు (TT) × పొట్టి (tt) → సంయోగబీజాలు T, t\nF1 తరం: అన్నీ Tt – పొడవు (పొడవు బహిర్గతం, పొట్టి అంతర్గతం)\nF1 ఆత్మ పరాగ సంపర్కం: Tt × Tt\n'
        'పునెట్ చతురస్రం | T | t\nT | TT (పొడవు) | Tt (పొడవు)\nt | Tt (పొడవు) | tt (పొట్టి)\n'
        'F2 దృశ్యరూప నిష్పత్తి = 3 పొడవు : 1 పొట్టి\nజన్యురూప నిష్పత్తి = 1 TT : 2 Tt : 1 tt')
SEX = ('తల్లి (XX) సంయోగబీజాలు → X, X\nతండ్రి (XY) సంయోగబీజాలు → X, Y\n'
       'పునెట్ చతురస్రం | X (తండ్రి) | Y (తండ్రి)\nX (తల్లి) | XX – ఆడపిల్ల | XY – మగపిల్లాడు\nX (తల్లి) | XX – ఆడపిల్ల | XY – మగపిల్లాడు\n'
       'ఆడ : మగ = 1 : 1 (50% : 50%)')
DI = ('గుండ్రని పసుపు (RRYY) × ముడతల ఆకుపచ్చ (rryy) → F1 అన్నీ RrYy (గుండ్రని పసుపు)\nF1 సంయోగబీజాలు: RY, Ry, rY, ry\n'
      '♂ \\ ♀ | RY | Ry | rY | ry\nRY | RRYY | RRYy | RrYY | RrYy\nRy | RRYy | RRyy | RrYy | Rryy\nrY | RrYY | RrYy | rrYY | rrYy\nry | RrYy | Rryy | rrYy | rryy\n'
      'F2: గుండ్రని పసుపు 9 : గుండ్రని ఆకుపచ్చ 3 : ముడతల పసుపు 3 : ముడతల ఆకుపచ్చ 1')
H, E = 'bi8', 'bi13'
ITEMS = [
# ══ 8. అనువంశికత ══ LEVEL-1
('QB1-08-8-1', H, 8, 'పునెట్ చతురస్రంతో మెండెల్ ఏకసంకరణ ప్రయోగాన్ని వివరించండి. (లేదా) లక్షణాలు బహిర్గతం లేదా అంతర్గతం కావచ్చని మెండెల్ ప్రయోగాలు ఎలా చూపుతాయి?',
 'మెండెల్ బఠాణీ మొక్కల్లో ఒకే జత విరుద్ధ లక్షణాన్ని (పొడవు/పొట్టి) తీసుకుని సంకరణం చేశాడు.\n' + MONO +
 '\nవివరణ: F1 లో పొట్టి లక్షణం కనిపించలేదు కానీ F2 లో మళ్ళీ కనిపించింది → F1 మొక్కలు పొడవు, పొట్టి రెండు లక్షణాల కారకాలను పొందాయి; ఒక జత కారకాలలో ఒకటే (పొడవు – బహిర్గతం) కనిపిస్తుంది, రెండవది (పొట్టి – అంతర్గతం) దాగి ఉంటుంది. రెండు అంతర్గత కారకాలు (tt) ఉంటేనే పొట్టి లక్షణం వ్యక్తమవుతుంది.',
 'Explain Mendel\'s monohybrid cross with a Punnett square. (OR) How do Mendel\'s experiments show that traits may be dominant or recessive?', 'TT × tt → F1 all Tt (tall). F1 selfed: Punnett square gives TT, 2 Tt, tt → F2 3 tall : 1 short (genotype 1 : 2 : 1). Shortness hidden in F1 reappears in F2 – tall is dominant, short is recessive.'),
('QB1-08-8-2', H, 8, 'మానవుల్లో లింగ నిర్ధారణను వివరించండి. (లేదా) శిశువు లింగం ఎలా నిర్ణయమవుతుంది?',
 'మానవుల్లో లింగం జన్యుపరంగా నిర్ణయమవుతుంది. 23 జతల క్రోమోజోముల్లో 22 జతలు జతలుగా ఒకేలా ఉంటాయి; 23వ జత లింగ క్రోమోజోములు.\nస్త్రీలలో: XX (సరైన జత), పురుషుల్లో: XY (Y చిన్నది).\n' + SEX +
 '\nవివరణ: తల్లి నుండి ఎప్పుడూ X క్రోమోజోమే వస్తుంది. తండ్రి నుండి X వస్తే ఆడపిల్ల (XX), Y వస్తే మగపిల్లాడు (XY). కాబట్టి శిశువు లింగాన్ని తండ్రి నుండి వచ్చే క్రోమోజోమే నిర్ణయిస్తుంది – దానికి తల్లిని నిందించడం తప్పు.',
 'Explain sex determination in human beings.', 'Women XX, men XY. The mother always gives X; if the father\'s sperm carries X the child is a girl (XX), if Y a boy (XY) – 50 : 50. The father\'s chromosome decides the sex.'),
('QB1-08-2-3', H, 2, 'బఠాణీ మొక్కలో మెండెల్ గమనించిన కనిపించే విరుద్ధ లక్షణాలు ఏవి?',
 'లక్షణం | బహిర్గతం | అంతర్గతం\nకాండం పొడవు | పొడవు | పొట్టి\nవిత్తన ఆకారం | గుండ్రని | ముడతలు\nవిత్తన రంగు | పసుపు | ఆకుపచ్చ\nపుష్ప రంగు | ఊదా | తెలుపు\n(ఇంకా: కాయ ఆకారం, కాయ రంగు, పుష్ప స్థానం)',
 'What contrasting visible characters did Mendel observe in pea plants?', 'Tall/short stem, round/wrinkled seed, yellow/green seed, violet/white flower (also pod shape, pod colour, flower position).'),
('QB1-08-2-4', H, 2, 'స్వప్న బహిర్గత, అంతర్గత రక్త వర్గ లక్షణాలు అధ్యయనం చేయాలనుకుంది. ఒక కుటుంబంలో తండ్రి, తల్లి, పిల్లల రక్త వర్గాలు సేకరించింది. బహిర్గత రక్త వర్గం తెలుసుకోవడానికి ఈ సమాచారం సరిపోతుందా? ఎందుకు?',
 'సరిపోదు. ఒక్క కుటుంబంలో పిల్లలు తక్కువ, సంభావ్య ఫలితాలు సరిగా కనిపించవు. అనేక కుటుంబాలు, అనేక తరాల సమాచారం (పెద్ద నమూనా) సేకరిస్తేనే ఏ లక్షణం బహిర్గతమో తెలుస్తుంది. (మెండెల్ వేల మొక్కలను పరిశీలించాడు.)',
 'Is the blood group data of one family enough to find the dominant blood group? Why?', 'No – one family gives too few offspring; data from many families and generations (a large sample) is needed.'),
('QB1-08-2-5', H, 2, 'మీ పాఠశాలలో లింగ సమానత్వ ప్రచారం జరుగుతోంది. చురుకైన భాగస్వామిగా మీరు ఎలా తోడ్పడతారు?',
 '1) శిశువు లింగాన్ని తండ్రి క్రోమోజోమే నిర్ణయిస్తుంది, కాబట్టి ఆడపిల్ల పుట్టిందని తల్లిని నిందించకూడదని వివరిస్తాను.\n2) బాలబాలికలకు సమాన విద్య, అవకాశాలు, పనుల్లో సమాన బాధ్యతపై నినాదాలు, ప్రదర్శనలు, నాటికలు నిర్వహిస్తాను; ఆడపిల్ల భ్రూణ హత్యలను వ్యతిరేకిస్తాను.',
 'How would you contribute to a gender equality campaign?', 'Explain that the father\'s chromosome decides the sex so mothers should not be blamed; promote equal education and opportunities through slogans, plays; oppose female foeticide.'),
('QB1-08-1-6', H, 1, 'అనువంశికత అంటే ఏమిటి?', 'తల్లిదండ్రుల లక్షణాలు సంతతికి సంక్రమించడమే అనువంశికత.', 'What is heredity?', 'Transmission of characters (traits) from parents to offspring.'),
('QB1-08-1-7', H, 1, 'DNA ని విస్తరించండి.', 'డీఆక్సీరైబో న్యూక్లియిక్ ఆమ్లం (Deoxyribonucleic Acid)', 'Expand DNA.', 'Deoxyribonucleic Acid'),
('QB1-08-1-8', H, 1, '“జన్యుశాస్త్ర పితామహుడు” ఎవరు?', 'గ్రెగర్ జోహాన్ మెండెల్',
 'Who is known as the Father of Genetics?', 'Gregor Johann Mendel', ['చార్లెస్ డార్విన్', 'లామార్క్', 'వాట్సన్'], '', ''),
('QB1-08-1-9', H, 1, 'అలైంగికంగా ప్రత్యుత్పత్తి చేసే జాతి జనాభాలో లక్షణం A 10% లో, లక్షణం B 60% లో ఉంది. ఏ లక్షణం ముందుగా ఏర్పడి ఉండవచ్చు?', 'లక్షణం B',
 'Trait A exists in 10% and trait B in 60% of an asexually reproducing population. Which trait arose earlier?', 'Trait B', ['లక్షణం A', 'రెండూ ఒకేసారి', 'చెప్పలేం'], 'ఎక్కువ తరాల పాటు సంక్రమించిన లక్షణం ఎక్కువ జీవుల్లో ఉంటుంది.', 'An older trait has spread to more individuals.'),
('QB1-08-1-10', H, 1, 'లింగ నిర్ధారణ పరిసరాల కారణాలతో జరిగే రెండు జీవుల పేర్లు రాయండి. (లేదా) లింగ నిర్ధారణ జన్యుపరం కాని రెండు ఉదాహరణలు?',
 'కొన్ని సరీసృపాలు (తాబేలు, మొసలి – గుడ్లు ఉంచిన ఉష్ణోగ్రతను బట్టి లింగం), నత్తలు (లింగం మార్చుకోగలవు).',
 'Name two organisms in which sex determination is regulated by environmental causes.', 'Some reptiles (turtle, crocodile – incubation temperature) and snails (can change sex).'),
('QB1-08-1-11', H, 1, 'పటం చూసి ఏకసంకరణ నిష్పత్తిని గుర్తించండి.\n' + IMG(I + 'qb_monohybrid.jpg', 'P → F1 → F2'), '3 : 1 (3 ఊదా : 1 తెలుపు పుష్పాలు)',
 'Observe the diagram and identify the monohybrid ratio.', '3 : 1', ['1 : 2 : 1', '9 : 3 : 3 : 1', '1 : 1'], 'F2 లో 3 ఊదా, 1 తెలుపు → దృశ్యరూప నిష్పత్తి 3 : 1.', 'F2 shows 3 violet : 1 white.'),
# ══ 8. అనువంశికత ══ LEVEL-2
('QB2-08-8-1', H, 8, 'పునెట్ చతురస్రంతో మెండెల్ ద్విసంకరణ ప్రయోగాన్ని వివరించండి. (లేదా) లక్షణాలు స్వతంత్రంగా సంక్రమిస్తాయని మెండెల్ ప్రయోగాలు ఎలా చూపుతాయి?',
 'మెండెల్ రెండు జతల విరుద్ధ లక్షణాలు (విత్తన ఆకారం – గుండ్రని/ముడతలు, విత్తన రంగు – పసుపు/ఆకుపచ్చ) తీసుకుని సంకరణం చేశాడు.\n' + DI +
 '\nవివరణ: F2 లో తల్లిదండ్రుల్లో లేని కొత్త కలయికలు (గుండ్రని ఆకుపచ్చ, ముడతల పసుపు) కనిపించాయి. అంటే విత్తన ఆకారం, రంగు లక్షణాలు ఒకదానితో ఒకటి సంబంధం లేకుండా స్వతంత్రంగా సంక్రమిస్తాయి.',
 'Explain Mendel\'s dihybrid cross with a Punnett square. (OR) How do Mendel\'s experiments show that traits are inherited independently?', 'RRYY × rryy → F1 RrYy (round yellow); F1 gametes RY, Ry, rY, ry; 4×4 Punnett square → F2 9 round yellow : 3 round green : 3 wrinkled yellow : 1 wrinkled green. New combinations show independent inheritance.'),
('QB2-08-8-2', H, 8, 'జీవుల్లో లక్షణాలు ఎలా వ్యక్తమవుతాయో వివరించండి. (లేదా) అనువంశికతలో జన్యువుల పాత్రను వివరించండి.',
 '1) కణ కేంద్రకంలోని DNA ప్రోటీన్ల తయారీకి సమాచార వనరు. ఒక ప్రోటీన్ తయారీకి సమాచారం ఇచ్చే DNA భాగమే జన్యువు.\n2) ప్రోటీన్లు (ఎంజైమ్‌లు, హార్మోన్లు) లక్షణాల వ్యక్తీకరణను నియంత్రిస్తాయి.\n3) ఉదా: మొక్క పొడవు – పెరుగుదల హార్మోన్ మీద ఆధారపడుతుంది. ఆ హార్మోన్ తయారీకి ఒక ఎంజైమ్ అవసరం. ఎంజైమ్ సమర్థంగా పనిచేస్తే ఎక్కువ హార్మోన్ → పొడవైన మొక్క. ఎంజైమ్ జన్యువులో మార్పు వల్ల ఎంజైమ్ సమర్థత తగ్గితే హార్మోన్ తక్కువ → పొట్టి మొక్క. కాబట్టి జన్యువులు లక్షణాలను నియంత్రిస్తాయి.\n4) లైంగిక ప్రత్యుత్పత్తిలో తల్లి, తండ్రి ఇద్దరూ సమానంగా DNA ఇస్తారు – ప్రతి లక్షణానికి రెండు జన్యు ప్రతులు (ఒకటి తల్లి నుండి, ఒకటి తండ్రి నుండి).\n5) ప్రతి సంయోగబీజానికి ఒక్కో జతలోంచి ఒక్క ప్రతి మాత్రమే వెళ్తుంది (క్రోమోజోములు జతలుగా ఉండి, సంయోగబీజాలకు ఒక్కోటి వెళ్తాయి) – ఇది జన్యువులు స్వతంత్రంగా సంక్రమించడాన్ని వివరిస్తుంది.',
 'Explain how traits get expressed in organisms (role of genes).', 'A gene is a section of DNA that provides information for one protein; proteins (enzymes, hormones) control traits – e.g. an efficient enzyme makes more growth hormone giving a tall plant. Each parent contributes one copy of each gene; gametes get one copy of each pair.'),
('QB2-08-2-3', H, 2, 'అన్ని వైవిధ్యాలు ఉపయోగకరమైనవని రాము, కొన్ని మాత్రమే ఉపయోగకరమని కృష్ణ అంటున్నారు. మీరు ఎవరిని సమర్థిస్తారు? ఎందుకు?',
 'కృష్ణను సమర్థిస్తాను. అన్ని వైవిధ్యాలు జీవికి లాభం చేయవు; కొన్ని హానికరం, కొన్ని ప్రభావం లేనివి. పరిసరాలు మారినప్పుడు జీవించడానికి సహాయపడే వైవిధ్యాలు మాత్రమే ఉపయోగకరం (ఉదా: వేడిని తట్టుకునే బ్యాక్టీరియా ఉష్ణ తరంగంలో బతుకుతాయి).',
 'Ramu says all variations are useful; Krishna says only some are. Whom do you support?', 'Krishna – only variations that help survival in a changed environment are useful; others may be harmful or neutral.'),
('QB2-08-1-4', H, 1, 'వైవిధ్యాలు అంటే ఏమిటి?', 'ఒకే జాతి జీవుల మధ్య (తల్లిదండ్రులు–సంతతి మధ్య) కనిపించే తేడాలే వైవిధ్యాలు.', 'What are variations?', 'Differences among individuals of the same species (between parents and offspring).'),
# ══ 13. మన పర్యావరణం ══ LEVEL-1
('QB1-13-4-1', E, 4, 'ఓజోన్ పొర దెబ్బతినడం ఎందుకు ఆందోళనకరం? ఈ నష్టాన్ని తగ్గించడానికి ఏ చర్యలు తీసుకుంటున్నారు?',
 'ఆందోళన: వాతావరణంలోని ఓజోన్ (O₃) పొర సూర్యుని నుండి వచ్చే హానికర అతినీలలోహిత (UV) కిరణాలను అడ్డుకుంటుంది. పొర పలుచబడితే UV కిరణాలు భూమిని చేరి మనుషుల్లో చర్మ క్యాన్సర్, కంటి శుక్లాలు, రోగనిరోధక శక్తి తగ్గడం, మొక్కలు–జంతువులకు నష్టం కలుగుతాయి.\nకారణం: రిఫ్రిజిరేటర్లు, అగ్నిమాపక యంత్రాల్లో వాడే క్లోరోఫ్లోరో కార్బన్లు (CFCs).\nచర్యలు: 1987 లో UNEP ఒప్పందం ద్వారా CFC ఉత్పత్తిని 1986 స్థాయిలోనే నిలిపివేయాలని నిర్ణయించారు; ఇప్పుడు CFC రహిత రిఫ్రిజిరేటర్లు తయారుచేస్తున్నారు; ప్రత్యామ్నాయ రసాయనాలు వాడుతున్నారు.',
 'Why is damage to the ozone layer a concern? What steps are taken to minimise it?', 'The ozone layer shields the earth from UV radiation which causes skin cancer etc.; CFCs damage it. In 1987 UNEP agreed to freeze CFC production at 1986 levels; CFC-free refrigerators are now made.'),
('QB1-13-4-2', E, 4, 'వ్యర్థాల నిర్వహణపై నాలుగు నినాదాలు రాయండి.',
 '1) “తడి చెత్త – పొడి చెత్త వేరు చేయండి, పరిసరాలు శుభ్రం చేయండి!”\n2) “తగ్గించు – మళ్ళీ వాడు – పునర్వినియోగం చేయి (Reduce, Reuse, Recycle)!”\n3) “చెత్తను కాల్చకు – కంపోస్ట్‌గా మార్చు!”\n4) “స్వచ్ఛ పరిసరాలు – స్వస్థ జీవితం!”',
 'Write four slogans on waste management.', '"Segregate wet and dry waste!" • "Reduce, Reuse, Recycle!" • "Don\'t burn waste, compost it!" • "Clean surroundings, healthy life!"'),
('QB1-13-4-3', E, 4, 'ప్లాస్టిక్ వ్యర్థాలను తగ్గించడానికి నాలుగు పర్యావరణ అనుకూల పద్ధతులు సూచించండి.',
 '1) దుకాణాలకు గుడ్డ/జనప సంచులు తీసుకెళ్లాలి.\n2) ఒక్కసారి వాడి పారేసే ప్లాస్టిక్ (గ్లాసులు, స్ట్రాలు, ప్లేట్లు) బదులు స్టీల్, గాజు, ఆకు విస్తర్లు వాడాలి.\n3) ప్లాస్టిక్ సీసాలు, డబ్బాలను మళ్ళీ వాడాలి; పునర్వినియోగానికి వేరుచేసి ఇవ్వాలి.\n4) ప్లాస్టిక్‌ను కాల్చకూడదు, నీటిలో వేయకూడదు; ప్లాస్టిక్ రహిత పాఠశాల కార్యక్రమాలు చేపట్టాలి.',
 'Suggest four eco-friendly practices to reduce plastic waste.', 'Use cloth/jute bags; steel, glass or leaf plates instead of single-use plastic; reuse and recycle plastic; never burn or dump plastic.'),
('QB1-13-2-4', E, 2, 'ఆవరణ వ్యవస్థలో విచ్ఛిన్నకారుల పాత్ర ఏమిటి?',
 'బ్యాక్టీరియా, శిలీంధ్రాలు వంటి విచ్ఛిన్నకారులు మృత మొక్కలు, జంతువుల శరీరాలు, వ్యర్థాలను సరళ పదార్థాలుగా విచ్ఛిన్నం చేస్తాయి. ఆ పోషకాలు మట్టిలోకి తిరిగి చేరి మొక్కలు మళ్ళీ వాడుకుంటాయి (పోషక చక్రం); పరిసరాలను శుభ్రంగా ఉంచుతాయి.',
 'What is the role of decomposers in an ecosystem?', 'Bacteria and fungi break down dead remains and wastes into simple substances that return to the soil for reuse by plants, keeping the environment clean.'),
('QB1-13-2-5', E, 2, 'జైవిక వృద్ధీకరణ (బయోమాగ్నిఫికేషన్) అంటే ఏమిటి? ఉదాహరణతో వివరించండి.',
 'విచ్ఛిన్నం కాని హానికర రసాయనాలు (క్రిమిసంహారకాలు వంటివి) ఆహార గొలుసులో ప్రతి పోషక స్థాయిలో క్రమంగా పేరుకుపోయి గాఢత పెరగడమే జైవిక వృద్ధీకరణ.\nఉదా: పంటలపై చల్లిన DDT → నీరు/మట్టి → మొక్కలు → శాకాహారులు → మాంసాహారులు → మనుషుల్లో (చివరి స్థాయిలో) అత్యధిక గాఢత.',
 'What is biomagnification? Explain with an example.', 'Accumulation of non-biodegradable chemicals in increasing concentration at each trophic level, e.g. pesticides like DDT reach the highest levels in humans at the top of the food chain.'),
('QB1-13-2-6', E, 2, 'ఆవరణ వ్యవస్థలోని ప్రాథమిక వినియోగదారులందరినీ చంపేస్తే ఏమవుతుంది?',
 'ఉత్పత్తిదారుల (మొక్కల) సంఖ్య అదుపు లేకుండా పెరుగుతుంది; ఆహారం లేక ద్వితీయ, తృతీయ వినియోగదారులు చనిపోతాయి – ఆహార గొలుసు తెగి ఆవరణ వ్యవస్థ సమతుల్యత దెబ్బతింటుంది.',
 'What will happen if we kill all the primary consumers in an ecosystem?', 'Producers would increase unchecked and higher consumers would starve – the food chain breaks and the ecosystem becomes unbalanced.'),
('QB1-13-2-7', E, 2, 'మీ పాఠశాలలో పర్యావరణ పరిరక్షణ అవగాహన కార్యక్రమం జరుగుతోంది. మీరు ఎలా పాల్గొంటారు?',
 '1) మొక్కలు నాటడం, చెత్తను తడి–పొడిగా వేరుచేయడం, ప్లాస్టిక్ వద్దు అనే ప్రచారంలో పాల్గొంటాను.\n2) నినాదాలు, పోస్టర్లు, ర్యాలీ, నీరు–విద్యుత్ పొదుపుపై గ్రామంలో అవగాహన కల్పిస్తాను.',
 'How would you participate in an environmental awareness programme in your school?', 'Plant trees, segregate waste, campaign against plastic, make posters and rallies, spread awareness on saving water and electricity.'),
('QB1-13-1-8', E, 1, 'CFC ని విస్తరించండి.', 'క్లోరోఫ్లోరో కార్బన్లు (Chlorofluorocarbons)', 'Expand CFC.', 'Chlorofluorocarbons'),
('QB1-13-1-9', E, 1, 'ఒక పోషక స్థాయి నుండి తర్వాతి స్థాయికి ఎంత శక్తి బదిలీ అవుతుంది?', '10%',
 'How much energy is transferred from one trophic level to the next?', '10%', ['50%', '1%', '90%'], 'పది శాతం నియమం – మిగిలినది ఉష్ణంగా, జీవక్రియల్లో ఖర్చవుతుంది.', 'The 10 per cent law.'),
('QB1-13-1-10', E, 1, 'ఆహార గొలుసులో ఉత్పత్తిదారు, శాకాహారి ఏవి? గడ్డి → గొల్లభామ → కప్ప → పాము → గద్ద',
 'ఉత్పత్తిదారు: గడ్డి; శాకాహారి (ప్రాథమిక వినియోగదారు): గొల్లభామ',
 'In the food chain Grass → Grasshopper → Frog → Snake → Eagle, which are the producer and herbivore?', 'Producer: grass; herbivore: grasshopper'),
# ══ 13. మన పర్యావరణం ══ LEVEL-2
('QB2-13-8-1', E, 8, 'వ్యవసాయంలో రసాయన క్రిమిసంహారకాల వాడకాన్ని తగ్గించే పద్ధతులు సూచించండి.',
 'ఎందుకు తగ్గించాలి: క్రిమిసంహారకాలు మట్టి, నీటిలో కలిసి మొక్కల ద్వారా ఆహార గొలుసులోకి చేరి జైవిక వృద్ధీకరణ వల్ల మనుషుల్లో ఎక్కువగా పేరుకుపోతాయి; మిత్ర కీటకాలు, పక్షులు చనిపోతాయి.\nపద్ధతులు:\n1) సేంద్రియ వ్యవసాయం – వేప కషాయం, వేప పిండి వంటి సహజ కీటక నాశకాలు.\n2) జీవ నియంత్రణ – పంటను తినే కీటకాలను తినే మిత్ర కీటకాలు (లేడీబర్డ్ వంటివి), పక్షులను ప్రోత్సహించడం.\n3) పంట మార్పిడి, మిశ్రమ పంటలు – తెగుళ్ల చక్రం తెగుతుంది.\n4) తెగుళ్లను తట్టుకునే రకాల విత్తనాలు వాడడం.\n5) లింగాకర్షక బుట్టలు (ఫెరోమోన్ ట్రాప్స్), లైట్ ట్రాప్స్, పసుపు జిగురు అట్టలు.\n6) సమగ్ర సస్యరక్షణ (IPM) – అవసరమైనప్పుడు మాత్రమే, సిఫార్సు చేసిన మోతాదులో.\n7) రైతులకు అవగాహన, శిక్షణ.',
 'Suggest methods to reduce chemical pesticides in agriculture.', 'Organic farming (neem extracts), biological control with predator insects/birds, crop rotation and mixed cropping, resistant varieties, pheromone/light traps, integrated pest management – because pesticides cause biomagnification and harm useful organisms.'),
('QB2-13-8-2', E, 8, 'వ్యర్థాల నిర్మూలనలో కాల్చడం, కంపోస్టింగ్‌లలో ఏది మంచిది? సరైన కారణాలతో సమర్థించండి.',
 'కంపోస్టింగ్ మంచిది.\nకాల్చడం వల్ల నష్టాలు:\n1) పొగ, కార్బన్ మోనాక్సైడ్, డయాక్సిన్లు వంటి విష వాయువులు వెలువడి వాయు కాలుష్యం.\n2) శ్వాసకోశ వ్యాధులు, కంటి సమస్యలు.\n3) ప్లాస్టిక్ కాలిస్తే మరింత హానికర వాయువులు.\n4) వ్యర్థాల్లోని పోషకాలు వృథా; గ్లోబల్ వార్మింగ్‌కు కారణం.\nకంపోస్టింగ్ లాభాలు:\n1) జీవ విచ్ఛిన్నం చెందే వ్యర్థాలను (కూరగాయల తొక్కలు, ఆకులు) సూక్ష్మజీవులు ఎరువుగా మారుస్తాయి.\n2) మట్టి సారం పెరుగుతుంది; రసాయన ఎరువుల అవసరం తగ్గుతుంది.\n3) కాలుష్యం ఉండదు; చెత్త పరిమాణం తగ్గుతుంది.\n4) వర్మీ కంపోస్ట్ ద్వారా ఆదాయం కూడా.\nకాబట్టి తడి చెత్తను కంపోస్ట్ చేసి, ప్లాస్టిక్ వంటి వాటిని పునర్వినియోగానికి పంపాలి.',
 'Which is better for waste disposal – burning or composting? Justify.', 'Composting – it turns biodegradable waste into manure without pollution, enriching soil; burning releases toxic gases, causes respiratory diseases and wastes nutrients.'),
('QB2-13-2-3', E, 2, 'ఆహార గొలుసుల్లో మూడు లేదా నాలుగు పోషక స్థాయిలే ఎందుకు ఉంటాయో ఊహించండి.',
 'ప్రతి పోషక స్థాయిలో 10% శక్తి మాత్రమే తర్వాతి స్థాయికి చేరుతుంది. నాలుగు–ఐదు స్థాయిల తర్వాత మిగిలే శక్తి చాలా తక్కువ – అది మరో స్థాయి జీవులను పోషించడానికి సరిపోదు.',
 'Predict why food chains have only three or four trophic levels.', 'Only 10% of energy passes to the next level, so after 3–4 levels too little energy remains to support another level.'),
('QB2-13-2-4', E, 2, 'ఆవరణ వ్యవస్థలో విచ్ఛిన్నకారులు లేకపోతే ఏమవుతుంది?',
 'మృత జీవులు, వ్యర్థాలు విచ్ఛిన్నం కాక పేరుకుపోతాయి; పోషకాలు మట్టికి తిరిగి చేరవు → మొక్కలకు పోషకాలు కరువై ఆవరణ వ్యవస్థ దెబ్బతింటుంది.',
 'What happens if there are no decomposers?', 'Dead bodies and wastes would pile up and nutrients would not return to the soil, so plants would lack nutrients.'),
('QB2-13-2-5', E, 2, 'ఆవరణ వ్యవస్థ నుండి వేటాడే జీవులు/మాంసాహారులను తొలగిస్తే ఏమవుతుంది?',
 'శాకాహారుల సంఖ్య అదుపు లేకుండా పెరిగి మొక్కలను అతిగా తినేస్తాయి → వృక్ష సంపద తగ్గి చివరకు ఆహార కొరతతో శాకాహారులూ చనిపోతాయి; ఆవరణ సమతుల్యత దెబ్బతింటుంది.',
 'What would happen if predators were removed from an ecosystem?', 'Herbivores would multiply, overgraze plants and later die of food shortage – the balance is disturbed.'),
('QB2-13-2-6', E, 2, '“ఒక పోషక స్థాయిలోని జీవులన్నింటినీ తొలగిస్తే మొత్తం ఆహార గొలుసుపై దుష్ప్రభావం పడుతుంది.” మీరు ఏకీభవిస్తారా? సమర్థించండి.',
 'ఏకీభవిస్తాను. ఆహార గొలుసులో ప్రతి స్థాయి ఒకదానిపై ఒకటి ఆధారపడి ఉంటుంది. ఒక స్థాయి తొలగిస్తే దాని పై స్థాయి ఆహారం లేక నశిస్తుంది, కింది స్థాయి అదుపు లేకుండా పెరుగుతుంది – మొత్తం గొలుసు, ఆవరణ సమతుల్యత దెబ్బతింటాయి.',
 '"Eliminating all organisms in one trophic level affects the entire food chain." Do you agree?', 'Yes – the level above starves and the level below multiplies unchecked, disturbing the whole chain.'),
('QB2-13-1-7', E, 1, 'ఆవరణ వ్యవస్థలో ఉత్పత్తిదారులందరూ చనిపోతే ఏమవుతుంది?', 'సౌరశక్తిని ఆహారంగా మార్చేవారు లేక ఆహార గొలుసు ప్రారంభం కాదు; వినియోగదారులందరూ క్రమంగా ఆహారం లేక చనిపోతారు.',
 'What happens if all producers die in an ecosystem?', 'No food would be made from sunlight, so all consumers would eventually die.'),
('QB2-13-1-8', E, 1, 'ఆహార గొలుసులో శక్తి ప్రవాహ దిశ ఏమిటి?', 'ఏకదిశ – ఉత్పత్తిదారుల నుండి వినియోగదారుల వైపు (వెనక్కి రాదు)',
 'What is the direction of energy flow in a food chain?', 'Unidirectional – from producers to consumers', ['ద్విదిశ', 'వినియోగదారుల నుండి ఉత్పత్తిదారులకు', 'వృత్తాకారం'], 'సూర్యుడు → ఉత్పత్తిదారులు → శాకాహారులు → మాంసాహారులు.', 'Sun → producers → herbivores → carnivores.'),
]
