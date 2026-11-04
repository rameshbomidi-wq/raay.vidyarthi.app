"""రాయ్ విద్యార్థి – 10వ తరగతి SSC ప్రశ్న–జవాబు బ్యాంక్ (ssc-10.js) తయారీ.
1 మార్కు: పాఠాల qz (బహుళైచ్ఛిక) + wb.qz + చిన్న qa జవాబులు; 2 మార్కులు: పెద్ద qa జవాబులు (ఆటో, notes-10.js నుండి)
4 / 8 మార్కులు: long_<sub>.py లోని ITEMS = [(lesson_id, marks, q_te, a_te, q_en, a_en), ...] (చేతితో రాసినవి; ద్విభాషా)
అంశం (item) రూపం: [lesson_id, marks, q, a, options|0, q_en|'', a_en|'']
"""
import json, os, glob, importlib.util
H = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(os.path.dirname(H))
src = open(f'{REPO}/notes-10.js', encoding='utf-8').read()
TB = json.loads(src[src.index(')[10]=') + 6:].rstrip().rstrip(';'))
import random, zlib
def hash_(t): return zlib.crc32(t.encode('utf-8'))
WQ = {  # పదం → అర్థం, అర్థం → పదం
 'tel': ('“{}” అనే పదానికి అర్థం?', '“{}” అనే అర్థం వచ్చే పదం?'), 'te2': ('“{}” అనే పదానికి అర్థం?', '“{}” అనే అర్థం వచ్చే పదం?'),
 'hin': ('“{}” शब्द का अर्थ (తెలుగులో)?', '“{}” – इस अर्थ वाला हिंदी शब्द?'), 'eng': ('Meaning of the word “{}”?', 'Which word means “{}”?'),
 'mat': ('“{}” ని English లో ఏమంటారు?', '“{}” అనే English పదానికి తెలుగు పదం?'), 'phy': ('“{}” ని English లో ఏమంటారు?', '“{}” అనే English పదానికి తెలుగు పదం?'),
 'bio': ('“{}” ని English లో ఏమంటారు?', '“{}” అనే English పదానికి తెలుగు పదం?'), 'soc': ('“{}” ని English లో ఏమంటారు?', '“{}” అనే English పదానికి తెలుగు పదం?')}
LQ = {'tel': ('“{}” పాఠ్యాంశ సారాంశం రాయండి.', '“{}” పాఠ్యాంశంలోని ముఖ్యాంశాలను వివరించండి.'),
      'te2': ('“{}” పాఠ్యాంశ సారాంశం రాయండి.', '“{}” పాఠ్యాంశంలోని ముఖ్యాంశాలను వివరించండి.'),
      'eng': ('Write the summary of “{}”.', 'Explain the main points of “{}”.')}
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
    # పదాల అర్థాలు → 1 మార్కు బహుళైచ్ఛిక (రెండు దిశల్లో) – పాఠంలోని ముఖ్య పదాల నుండి ఆటో
    allw = [(L['id'], w[0].strip(), w[1].strip()) for L in lessons for w in L.get('w', []) if len(w) >= 2 and w[0].strip() and w[1].strip()]
    for i, (lid, wd, mn) in enumerate(allw):
        for qn, (q, ans, key) in enumerate(((WQ[s][0].format(wd), mn, 2), (WQ[s][1].format(mn), wd, 1))):
            if len(ans) > 70 or q in seen: continue
            pool = [x[key] for x in allw if x[key] != ans and x[key] not in (wd, mn) and len(x[key]) <= 70]
            pool = list(dict.fromkeys(pool))
            if len(pool) < 3: continue
            rnd = random.Random(hash_(q)); same = [x[key] for x in allw if x[0] == lid and x[key] in pool]
            opts = (rnd.sample(same, min(2, len(same))) if same else [])
            rest = [x for x in pool if x not in opts]; opts += rnd.sample(rest, 3 - len(opts))
            seen.add(q); items.append([lid, 1, q, ans, opts, '', ''])
    # భాషా పాఠాలు → 4 మార్కులు (సారాంశం), 8 మార్కులు (ముఖ్యాంశాలు) – sum/pts నుండి
    if s in LQ:
        for L in lessons:
            if L.get('sum'): items.append([L['id'], 4, LQ[s][0].format(L['t']), L['sum'], 0, '', ''])
            if len(L.get('pts', [])) >= 4: items.append([L['id'], 8, LQ[s][1].format(L['t']), '\n'.join('• ' + x for x in L['pts']), 0, '', ''])
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
