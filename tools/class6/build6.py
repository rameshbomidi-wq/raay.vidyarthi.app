# 6వ తరగతి పాఠ్యపుస్తకం నోట్స్ + జవాబులు → notes-6.js, answers-6.js
# ప్రతి పాఠం ch/<పేరు>.py: S (సబ్జెక్టు), BK (పుస్తకం కీ, లేకపోతే S), PAGES (PDF పరిధి), L (పాఠం dict), SEC = [(PDF పేజీ, శీర్షిక, [జవాబులు])]
# ఉన్న notes-6.js / answers-6.js లోని ఇతర పాఠాలు (ఇక్కడ ch/ లో లేనివి) అలాగే ఉంటాయి.
import json, glob, importlib.util, os
H = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(f'{H}/../..')
BOOK = {'mat': ('Class6_Maths_Textbook_Sem1.pdf', 8), 'sci': ('Class6_Science_Textbook_Sem1.pdf', 8), 'soc': ('Class6_Social_Textbook_Sem1.pdf', 8)}
BIL = {'mat', 'sci', 'soc'}  # సరి పేజీ English, తర్వాతి (బేసి) పేజీ తెలుగు → జవాబులు రెండింటికీ
def load(f):
    sp = importlib.util.spec_from_file_location('c6_' + os.path.basename(f)[:-3], f); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
def rd(fn, key):
    p = f'{REPO}/{fn}'
    if not os.path.exists(p): return {}
    src = open(p).read(); return json.loads(src[src.index(key) + len(key):].rstrip().rstrip(';'))
out = {}; ANS = {}
for f in sorted(glob.glob(f'{H}/ch/*.py')):
    m = load(f); L = dict(m.L); s = m.S; k = getattr(m, 'BK', s); bk, off = BOOK[k]; a, b = m.PAGES
    W = dict(L.get('wb', {})); W.update(pg=f'{a-off}–{b-off}', f=f'books/6/{bk}', p=a, lb=getattr(m, 'WLB', 'పాఠ్యపుస్తకం'))
    tg = []; ws = []; A = ANS.setdefault(bk, {})
    for pg, title, items in m.SEC:
        lines = [p.strip() for it in items for p in it.split(' | ')]
        t = f'{title} (పుట {pg-off})'; tg.append([t, lines]); ws.append(t)
        A.setdefault(str(pg), []).extend([f'— {title} —'] + lines)
        if k in BIL: A.setdefault(str(pg + 1), []).extend([f'— {title} —'] + lines)
    W['ws'] = ws; L['wb'] = W; L['tg'] = tg + list(L.get('tg', []))
    assert len(L['qz']) >= 10, L['id']
    for z in L['qz'] + W.get('qz', []): assert len(z) == 5 and len(set(z[1:])) == 4, (L['id'], z)
    out.setdefault(s, []).append(L)
cur = rd('notes-6.js', ')[6]=')
for s, ls in out.items():
    ids = {x['id'] for x in ls}; keep = [x for x in cur.get(s, []) if x['id'] not in ids]
    cur[s] = ls + keep
for s in cur: cur[s].sort(key=lambda x: x['no'])
js = '/* రాయ్ విద్యార్థి – 6వ తరగతి పాఠ్యపుస్తకం నోట్స్ (సెమిస్టర్-1) */\n(window.RAAY_TB=window.RAAY_TB||{})[6]=' + json.dumps(cur, ensure_ascii=False, separators=(',', ':')) + ';\n'
open(f'{REPO}/notes-6.js', 'w').write(js)
ca = rd('answers-6.js', ')[6]=')
for bk, v in ANS.items(): ca[bk] = {p: v[p] for p in sorted(v, key=int)}
aj = '/* రాయ్ విద్యార్థి – 6వ తరగతి పాఠ్యపుస్తక ప్రశ్నల జవాబులు (టీచర్ లాక్ తెరిస్తేనే) */\n(window.RAAY_ANS=window.RAAY_ANS||{})[6]=' + json.dumps(ca, ensure_ascii=False, separators=(',', ':')) + ';\n'
open(f'{REPO}/answers-6.js', 'w').write(aj)
print({s: [(x['id'], len(x['qz']), len(x['tg'])) for x in out[s]] for s in out}, 'notes', len(js), 'answers', len(aj))
