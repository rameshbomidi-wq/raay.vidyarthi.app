# 9వ తరగతి పాఠ్యపుస్తకం నోట్స్ + జవాబులు → notes-9.js, answers-9.js (ఉన్న ఇతర పాఠాలు – SA1 మోడల్ పేపర్లు – అలాగే ఉంటాయి)
# ప్రతి పాఠం ch/<పేరు>.py: S (సబ్జెక్టు), BK (పుస్తకం కీ), PAGES (PDF పరిధి), L (పాఠం dict), SEC = [(PDF పేజీ, శీర్షిక, [జవాబులు])]
import json, glob, importlib.util, os
H = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(f'{H}/../..')
BOOK = {'mat': ('Class9_Maths_Textbook_Sem1.pdf', 10), 'phy': ('Class9_Physical_Science_Textbook_Sem1.pdf', 6), 'bio': ('Class9_Biology_Textbook_Sem1.pdf', -140),
        'soc': ('Class9_Social_Textbook_Sem1.pdf', 6), 'tel': ('Class9_Telugu_Textbook_Sem1.pdf', 6), 'hin': ('Class9_Hindi_Textbook_Sem1.pdf', -120),
        'eng': ('Class9_English_Textbook_Sem1.pdf', -160), 'te2': ('Class9_Telugu_SecondLanguage_Textbook.pdf', 8)}
BIL = {'mat', 'phy', 'bio', 'soc'}  # సరి పేజీ English, తర్వాతి పేజీ తెలుగు → జవాబులు రెండింటికీ
def load(f):
    sp = importlib.util.spec_from_file_location('c9_' + os.path.basename(f)[:-3], f); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
out = {}; ANS = {}
for f in sorted(glob.glob(f'{H}/ch/*.py')):
    m = load(f); L = dict(m.L); s = m.S; k = getattr(m, 'BK', s); bk, off = BOOK[k]; a, b = m.PAGES
    W = dict(L.get('wb', {})); W.update(pg=f'{a-off}–{b-off}', f=f'books/9/{bk}', p=a, lb=getattr(m, 'WLB', 'పాఠ్యపుస్తకం'))
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
src = open(f'{REPO}/notes-9.js').read(); cur = json.loads(src[src.index(')[9]=') + 5:].rstrip().rstrip(';'))
for s, ls in out.items():
    ids = {x['id'] for x in ls}; keep = [x for x in cur.get(s, []) if x['id'] not in ids]
    cur[s] = sorted(ls, key=lambda x: x['no']) + keep   # కొత్త పాఠాలు ముందు, SA1 పేపర్లు (no 101+) తర్వాత
for s in cur: cur[s].sort(key=lambda x: x['no'])
js = '/* రాయ్ విద్యార్థి – 9వ తరగతి పాఠ్యపుస్తకం నోట్స్ + SA1 మోడల్ పేపర్లు */\n(window.RAAY_TB=window.RAAY_TB||{})[9]=' + json.dumps(cur, ensure_ascii=False, separators=(',', ':')) + ';\n'
open(f'{REPO}/notes-9.js', 'w').write(js)
src = open(f'{REPO}/answers-9.js').read(); ca = json.loads(src[src.index(')[9]=') + 5:].rstrip().rstrip(';'))
for bk, v in ANS.items(): ca[bk] = {p: v[p] for p in sorted(v, key=int)}
aj = src[:src.index('(window.RAAY_ANS')] + '(window.RAAY_ANS=window.RAAY_ANS||{})[9]=' + json.dumps(ca, ensure_ascii=False, separators=(',', ':')) + ';\n'
open(f'{REPO}/answers-9.js', 'w').write(aj)
print({s: [(x['id'], len(x['qz']), len(x['tg'])) for x in out[s]] for s in out}, 'notes', len(js), 'answers', len(aj))
