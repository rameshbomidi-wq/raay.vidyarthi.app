"""10వ తరగతి గణితం నోట్స్‌కు పటాలు/పట్టికలు – notes-10.js లో పాఠానికి `fg` = [[శీర్షిక, టెక్స్ట్ (⟦fig⟧ / | పట్టిక)], ...]
పరుగు: python3 tools/class10_math/notes_figs.py  (మళ్ళీ పరిగెత్తినా సరే – fg మార్చి రాస్తుంది). తర్వాత build_ssc.py అవసరం లేదు.
"""
import os, sys, json, importlib.util, math
H = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(os.path.dirname(H))
sys.path.insert(0, os.path.join(REPO, 'tools'))
from figlib import F, P, S, PG, A, R, M, T
sp = importlib.util.spec_from_file_location('fm', os.path.join(REPO, 'tools/ssc10/figs_mat.py')); fm = importlib.util.module_from_spec(sp); sp.loader.exec_module(fm)
rt, tower = fm.rt, fm.tower

FG = {
'ma8': [
 ['లంబకోణ త్రిభుజం – భుజాల పేర్లు', rt(6, 4, ('ఆసన్న భుజం', 'ఎదుటి భుజం', 'కర్ణం'), w=300,
   cap='∠A = θ కి: ఎదుటి భుజం BC, ఆసన్న భుజం AB, కర్ణం AC (లంబకోణానికి ఎదురుగా – అతి పొడవైనది)')],
 ['త్రికోణమితి నిష్పత్తులు', 'నిష్పత్తి | నిర్వచనం | వ్యుత్క్రమం\nsin θ | ఎదుటి భుజం / కర్ణం | cosec θ = 1/sin θ\ncos θ | ఆసన్న భుజం / కర్ణం | sec θ = 1/cos θ\ntan θ | ఎదుటి భుజం / ఆసన్న భుజం | cot θ = 1/tan θ\ntan θ = sin θ / cos θ,  cot θ = cos θ / sin θ'],
 ['45° త్రిభుజం', rt(4, 4, ('a', 'a', '√2 a'), th='45°', th2='45°', w=230, cap='sin 45° = cos 45° = 1/√2, tan 45° = 1')],
 ['30° – 60° త్రిభుజం (సమబాహు త్రిభుజంలో సగం)', F([-1.2, 6.0, -1.0, 4.3], PG([[0, 0], [4, 0], [2, 3.464]], fm.FILL), S(2, 3.464, 2, 0, 'd'), R(2, 0, 0, 90, 0.25),
   A(0, 0, 0.8, 0, 60, '60°'), A(2, 3.464, 0.9, 240, 270, '30°'), P(0, 0, 'B', 'sw'), P(4, 0, 'C', 'se'), P(2, 3.464, 'A', 'n'), P(2, 0, 'D', 's'),
   M(0, 0, 2, 0, 'a', 1), M(0, 0, 2, 3.464, '2a', -1), M(2, 3.464, 2, 0, '√3 a', 1), w=260,
   cap='ΔABD లో: sin 30° = a/2a = 1/2, cos 30° = √3/2, tan 30° = 1/√3; sin 60° = √3/2, cos 60° = 1/2, tan 60° = √3')],
 ['ప్రామాణిక కోణాల విలువలు (కంఠస్థం చేయండి)', '∠A | 0° | 30° | 45° | 60° | 90°\nsin A | 0 | 1/2 | 1/√2 | √3/2 | 1\ncos A | 1 | √3/2 | 1/√2 | 1/2 | 0\ntan A | 0 | 1/√3 | 1 | √3 | —\ncosec A | — | 2 | √2 | 2/√3 | 1\nsec A | 1 | 2/√3 | √2 | 2 | —\ncot A | — | √3 | 1 | 1/√3 | 0\n— = నిర్వచింపబడదు • చిట్కా: sin విలువలు √0/2, √1/2, √2/2, √3/2, √4/2; cos వాటికి తిరగబడి.'],
 ['త్రికోణమితీయ సర్వసమీకరణాలు', 'సర్వసమీకరణం | ఎలా వస్తుంది (AB² + BC² = AC²)\nsin²A + cos²A = 1 | AC² తో భాగిస్తే\n1 + tan²A = sec²A | AB² తో భాగిస్తే\n1 + cot²A = cosec²A | BC² తో భాగిస్తే'],
],
'ma9': [
 ['ఊర్ధ్వ కోణం (Angle of elevation)', fm.ELEV],
 ['నిమ్న కోణం (Angle of depression)', fm.DEPR],
 ['రెండూ ఒకే పటంలో', fm.BOTH],
 ['ఉదాహరణ 1: టవర్ ఎత్తు', tower(3, 1.732, '30°', '30 మీ.', 'h', w=260, cap='tan 30° = h/30 → h = 30/√3 = 10√3 మీ. ≈ 17.32 మీ.')],
 ['ఉదాహరణ 2: నది వెడల్పు', fm.BRIDGE],
 ['ఉదాహరణ 3: రెండు భవనాలు', fm.TWOB],
 ['సమస్య సాధన – అడుగులు', 'అడుగు | ఏమి చేయాలి\n1 | పటం గీసి, క్షితిజ సమాంతర రేఖ, లంబకోణం గుర్తించండి\n2 | ఇచ్చిన కోణాలు, కొలతలు పటంపై రాయండి (నిమ్న కోణం = కింది బిందువు వద్ద ఊర్ధ్వ కోణం)\n3 | తెలిసిన భుజం, కావలసిన భుజం ఉన్న నిష్పత్తి ఎంచుకోండి (ఎత్తు–దూరం అయితే tan)\n4 | సమీకరణం సాధించి, యూనిట్లతో జవాబు రాయండి (√3 ≈ 1.732)'],
],
}

src = open(os.path.join(REPO, 'notes-10.js'), encoding='utf-8').read()
pre = src[:src.index(')[10]=') + 6]
cur = json.loads(src[len(pre):].rstrip().rstrip(';'))
n = 0
for L in cur['mat']:
    if L['id'] in FG: L['fg'] = FG[L['id']]; n += 1
assert n == len(FG)
open(os.path.join(REPO, 'notes-10.js'), 'w', encoding='utf-8').write(pre + json.dumps(cur, ensure_ascii=False, separators=(',', ':')) + ';\n')
print('fg', {k: len(v) for k, v in FG.items()})
