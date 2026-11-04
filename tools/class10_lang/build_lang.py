import json, glob, importlib.util, os, sys
H = os.path.dirname(os.path.abspath(__file__))
REPO = '/home/claude/raay.vidyarthi.app'
# subject -> (book file, pdf offset)
BOOK = {'tel': ('Class10_Telugu_Textbook_Sem1.pdf', 8), 'te2': ('Class10_Telugu_SecondLanguage_Textbook.pdf', 8), 'hin': ('Class10_Hindi_Textbook_Sem1.pdf', 2),
        'eng': ('Class10_English_Textbook_Sem1.pdf', 18), 'engw': ('Class10_English_Workbook_Sem1.pdf', 6), 'engr': ('Class10_English_SupplementaryReader_Sem1.pdf', 5)}

def load(f):
    sp = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m

out = {}; ANS = {}
for f in sorted(glob.glob(f'{H}/ch/*.py')):
    m = load(f); L = dict(m.L); s = m.S; bkey = getattr(m, 'BK', s)
    wkey = getattr(m, 'WBK', bkey); bk, off = BOOK[wkey]
    a, b = getattr(m, 'WPAGES', m.PAGES)  # pdf page range shown as wb
    W = dict(L.get('wb', {})); W.update(pg=f'{a-off}–{b-off}', f=f'books/10/{bk}', p=a, lb=getattr(m, 'WLB', 'పాఠ్యపుస్తకం'))
    tg = []; ws = []
    for sec in m.SEC:
        k, (pg, title, items) = (sec[0], sec[1:]) if len(sec) == 4 else (bkey, sec)
        sbk, soff = BOOK[k]; A = ANS.setdefault(sbk, {})
        lines = [p.strip() for it in items for p in it.split(' | ')]
        t = f'{title} (పుట {pg-soff})' + (' – వర్క్‌బుక్' if k == 'engw' else '')
        tg.append([t, lines]); ws.append(t)
        A.setdefault(str(pg), []).extend([f'— {title} —'] + lines)
    W['ws'] = ws; L['wb'] = W; L['tg'] = tg
    assert len(L['qz']) >= 10, L['id']
    for z in L['qz'] + W.get('qz', []): assert len(z) == 5 and len(set(z[1:])) == 4, (L['id'], z)
    out.setdefault(s, []).append(L)
for s in out: out[s].sort(key=lambda x: x['no'])
src = open(f'{REPO}/notes-10.js').read()
cur = json.loads(src[src.index(')[10]=') + 6:].rstrip().rstrip(';'))
cur.update(out)
js = '/* రాయ్ విద్యార్థి – 10వ తరగతి పాఠ్యపుస్తకం నోట్స్ */\n(window.RAAY_TB=window.RAAY_TB||{})[10]=' + json.dumps(cur, ensure_ascii=False, separators=(',', ':')) + ';\n'
open(f'{REPO}/notes-10.js', 'w').write(js)
src = open(f'{REPO}/answers-10.js').read()
ca = json.loads(src[src.index(')[10]=') + 6:].rstrip().rstrip(';'))
for bk, v in ANS.items(): ca[bk] = {p: v[p] for p in sorted(v, key=int)}
aj = '/* రాయ్ విద్యార్థి – 10వ తరగతి జవాబులు (పాఠ్యపుస్తకం PDF పేజీ వారీగా; టీచర్ లాక్ తెరిచాకే) */\n(window.RAAY_ANS=window.RAAY_ANS||{})[10]=' + json.dumps(ca, ensure_ascii=False, separators=(',', ':')) + ';\n'
open(f'{REPO}/answers-10.js', 'w').write(aj)
print({s: [(x['id'], len(x['qz']), len(x['tg'])) for x in out[s]] for s in out}, 'notes', len(js), 'answers', len(aj))
