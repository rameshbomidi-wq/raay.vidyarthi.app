# 3వ తరగతి సెమిస్టర్-2 పాఠ్యపుస్తకం నోట్స్ + జవాబులు → notes-3.js, answers-3.js (సెమ్-1 పాఠాలు అలాగే ఉంటాయి)
# ప్రతి పాఠం ch/<పేరు>.py: S (సబ్జెక్టు), BK (పుస్తకం కీ, లేకపోతే S), PAGES (PDF పరిధి), L (పాఠం dict),
# SEC = [(PDF పేజీ, శీర్షిక, [జవాబులు])]  – ' | ' తో విడగొట్టిన వరుసలు వేర్వేరు జవాబులుగా.
# పుస్తకాలు (యూజర్ పంపిన సెమ్-2 PDFలు, 110dpi JPEG): ముద్రిత పుట = PR[key](PDF పేజీ)
#   tel: ముద్రిత = PDF − 8 • eng: ముద్రిత = PDF + 48 • mat: తెలుగు పేజీలు మాత్రమే, ముద్రిత = 2×PDF − 1 • evs: తెలుగు పేజీలు మాత్రమే, ముద్రిత = 2×PDF + 151
import json, glob, importlib.util, os
H = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(f'{H}/../..')
BOOK = {'tel': 'Class3_Telugu_Textbook_Sem2.pdf', 'eng': 'Class3_English_Textbook_Sem2.pdf',
        'mat': 'Class3_Maths_Textbook_Sem2_Telugu.pdf', 'evs': 'Class3_EVS_Textbook_Sem2_Telugu.pdf'}
PR = {'tel': lambda p: p - 8, 'eng': lambda p: p + 48, 'mat': lambda p: 2 * p - 1, 'evs': lambda p: 2 * p + 151}
M = '⁂'  # జవాబుల దాపరికం (యాప్ unz: chr−7)
def Z(x):
    if not isinstance(x, str) or x.startswith(M) or any(ord(c) >= 0xCFF0 for c in x): return x
    return M + ''.join(chr(ord(c) + 7) for c in x)
def load(f):
    sp = importlib.util.spec_from_file_location('c3_' + os.path.basename(f)[:-3], f); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
def rd(fn, key):
    p = f'{REPO}/{fn}'
    if not os.path.exists(p): return {}
    src = open(p).read(); return json.loads(src[src.index(key) + len(key):].rstrip().rstrip(';'))
out = {}; ANS = {}
for f in sorted(glob.glob(f'{H}/ch/*.py')):
    m = load(f); L = dict(m.L); s = m.S; k = getattr(m, 'BK', s); bk = BOOK[k]; pr = PR[k]; a, b = m.PAGES
    W = dict(L.get('wb', {})); W.update(pg=f'{pr(a)}–{pr(b)}', f=f'books/3/{bk}', p=a, lb='పాఠ్యపుస్తకం')
    tg = []; ws = []; A = ANS.setdefault(bk, {})
    for pg, title, items in m.SEC:
        lines = [p.strip() for it in items for p in it.split(' | ')]
        t = f'{title} (పుట {pr(pg)})'; tg.append([t, lines]); ws.append(t)
        A.setdefault(str(pg), []).extend([f'— {title} —'] + lines)
    W['ws'] = ws
    wf = f'{H}/wb/w{L["id"][-1]}.py' if L['id'].startswith('ma') else None
    if wf and os.path.exists(wf):  # సెమ్-2 గణితం వర్క్‌బుక్ (PDF = ముద్రిత + 4; ఇంగ్లీష్/తెలుగు పేజీలు జతలు)
        wm = load(wf); WBK = 'Class3_Maths_Workbook_Sem2.pdf'; WA = ANS.setdefault(WBK, {}); wa, wb_ = wm.WB
        W = {k: v for k, v in W.items() if k not in ('lb',)}; W.update(pg=f'{wa - 4}–{wb_ - 4}', f=f'books/3/{WBK}', p=wa)
        wws = []
        for pgs, title, items in wm.WSEC:
            lines = [q.strip() for it in items for q in it.split(' | ')]
            t = f'📒 {title} (వర్క్‌బుక్ పుట {"/".join(str(x - 4) for x in pgs)})'; tg.append([t, lines]); wws.append(t)
            for pg in pgs: WA.setdefault(str(pg), []).extend([f'— {title} —'] + lines)
        W['ws'] = wws; W['tb'] = {'f': f'books/3/{bk}', 'p': a, 'pg': f'{pr(a)}–{pr(b)}', 'ws': ws}
    L['wb'] = W; L['tg'] = tg + list(L.get('tg', []))
    assert len(L['qz']) >= 10, L['id']
    for z in L['qz'] + W.get('qz', []): assert len(z) == 5 and len(set(z[1:])) == 4, (L['id'], z)
    out.setdefault(s, []).append(L)
cur = rd('notes-3.js', ')[3]=')
for s, ls in out.items():
    ids = {x['id'] for x in ls}; keep = [x for x in cur.get(s, []) if x['id'] not in ids]
    cur[s] = keep + ls
for s in cur:
    cur[s].sort(key=lambda x: x['no'])
    for x in cur[s]: x['tg'] = [[t, [Z(a) for a in ls]] for t, ls in x.get('tg', [])]
hd = open(f'{REPO}/notes-3.js').read().split('(window.RAAY_TB')[0]
js = hd + '(window.RAAY_TB=window.RAAY_TB||{})[3]=' + json.dumps(cur, ensure_ascii=False, separators=(',', ':')) + ';\n'
open(f'{REPO}/notes-3.js', 'w').write(js)
ca = rd('answers-3.js', ')[3]=')
for bk, v in ANS.items(): ca[bk] = {p: v[p] for p in sorted(v, key=int)}
ca = {bk: {p: [Z(a) for a in ls] for p, ls in v.items()} for bk, v in ca.items()}
ah = '/* రాయ్ విద్యార్థి యాప్ – 3వ తరగతి వర్క్‌బుక్ (సెమ్-1) + పాఠ్యపుస్తకం (సెమ్-2) జవాబులు. టీచర్ పాఠం వారీగా 🔓 తెరిచాకే పిల్లలకు కనిపిస్తాయి. */\n'
aj = ah + '(window.RAAY_ANS=window.RAAY_ANS||{})[3]=' + json.dumps(ca, ensure_ascii=False, separators=(',', ':')) + ';\n'
open(f'{REPO}/answers-3.js', 'w').write(aj)
print({s: [(x['id'], len(x['qz']), len(x['tg'])) for x in out[s]] for s in out}, 'notes', len(js), 'answers', len(aj))
