"""రాయ్ విద్యార్థి – 10వ తరగతి SSC ప్రశ్న–జవాబు బ్యాంక్ (ssc-10.js) తయారీ.
1 మార్కు: పాఠాల qz (బహుళైచ్ఛిక) + wb.qz + చిన్న qa జవాబులు; 2 మార్కులు: పెద్ద qa జవాబులు (ఆటో, notes-10.js నుండి)
4 / 8 మార్కులు: long_<sub>.py లోని ITEMS = [(lesson_id, marks, q_te, a_te, q_en, a_en), ...] (చేతితో రాసినవి; ద్విభాషా)
అంశం (item) రూపం: [lesson_id, marks, q, a, options|0, q_en|'', a_en|'']
"""
import json, os, glob, importlib.util
H = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(os.path.dirname(H))
src = open(f'{REPO}/notes-10.js', encoding='utf-8').read()
TB = json.loads(src[src.index(')[10]=') + 6:].rstrip().rstrip(';'))
EN = {}  # optional English for auto items: en_<sub>.py  T = {('q_te'): ('q_en','a_en')}
out = {}
for s, lessons in TB.items():
    items = []; seen = set()
    for L in lessons:
        lid = L['id']
        for z in L.get('qz', []) + (L.get('wb') or {}).get('qz', []):
            if z[0] in seen: continue
            seen.add(z[0]); items.append([lid, 1, z[0], z[1], z[2:5], '', ''])
        for q, a in L.get('qa', []):
            if q in seen: continue
            seen.add(q); items.append([lid, 1 if len(a) <= 70 else 2, q, a, 0, '', ''])
    out[s] = items
for f in sorted(glob.glob(f'{H}/long_*.py')):
    sp = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    s = os.path.basename(f)[5:-3]
    for it in m.ITEMS:
        lid, mk, q, a = it[:4]; qe = it[4] if len(it) > 4 else ''; ae = it[5] if len(it) > 5 else ''
        assert mk in (2, 4, 8) and any(L['id'] == lid for L in TB[s]), (s, lid)
        out[s].append([lid, mk, q, a, 0, qe, ae])
order = {L['id']: i for s in TB for i, L in enumerate(TB[s])}
for s in out: out[s].sort(key=lambda x: (order[x[0]], x[1]))
js = '/* రాయ్ విద్యార్థి – 10వ తరగతి SSC ప్రశ్న–జవాబు బ్యాంక్ (1/2/4/8 మార్కులు) – tools/ssc10/build_ssc.py తో తయారు */\n(window.RAAY_SSC=window.RAAY_SSC||{})[10]=' + json.dumps(out, ensure_ascii=False, separators=(',', ':')) + ';\n'
open(f'{REPO}/ssc-10.js', 'w', encoding='utf-8').write(js)
from collections import Counter
print({s: dict(Counter(x[1] for x in v)) for s, v in out.items()}, len(js))
