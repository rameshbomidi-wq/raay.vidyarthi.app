#!/usr/bin/env python3
"""10వ తరగతి పెద్ద ఫైళ్లను సబ్జెక్టు వారీగా విడగొడుతుంది (యాప్ వేగం కోసం).

notes-10.js  → notes-10-idx.js (పాఠాల పేర్లు/నెలలు/పుస్తకం పేజీలు మాత్రమే, _lite:1) + notes-10-<sub>.js (పూర్తి పాఠాలు)
ssc-10.js    → ssc-10-idx.js (సబ్జెక్టుల సంఖ్యలు + RAAY_MM/RAAY_SSC_BM/RAAY_SSC_LN) + ssc-10-<sub>.js

notes-10.js, ssc-10.js మూల ఫైళ్లుగా అలాగే ఉంటాయి (build_lang.py / build_ssc.py అవే రాస్తాయి).
వాటిని మార్చిన ప్రతిసారీ:  python3 tools/split/split_class10.py
"""
import json, subprocess, sys
from pathlib import Path
R = Path(__file__).resolve().parents[2]
C = 10

def node_eval(js):
    r = subprocess.run(['node', '-e', js], capture_output=True, text=True, cwd=R)
    if r.returncode: sys.exit(r.stderr)
    return json.loads(r.stdout)

def dump(o):
    return json.dumps(o, ensure_ascii=False, separators=(',', ':'))

def split_notes():
    d = node_eval(f"global.window={{}};require('./notes-{C}.js');process.stdout.write(JSON.stringify(window.RAAY_TB[{C}]))")
    idx = {}
    for s, ls in d.items():
        lite = []
        for L in ls:
            x = {k: L[k] for k in ('id', 'no', 't', 'm', 'ty') if k in L}
            if L.get('wb'):
                x['wb'] = {k: L['wb'][k] for k in ('pg', 'f', 'p', 'lb') if k in L['wb']}
            x['_lite'] = 1
            lite.append(x)
        idx[s] = lite
        (R / f'notes-{C}-{s}.js').write_text(
            f"/* {C}వ తరగతి – {s} పూర్తి పాఠాలు (tools/split/split_class10.py) */\n"
            f"((window.RAAY_TBF=window.RAAY_TBF||{{}})[{C}]=window.RAAY_TBF[{C}]||{{}})[{json.dumps(s)}]={dump(ls)};\n", encoding='utf-8')
    (R / f'notes-{C}-idx.js').write_text(
        f"/* {C}వ తరగతి పాఠాల సూచిక – పూర్తి పాఠం notes-{C}-<సబ్జెక్టు>.js నుండి అవసరమైనప్పుడు (tools/split/split_class10.py) */\n"
        f"(window.RAAY_TB=window.RAAY_TB||{{}})[{C}]={dump(idx)};\n", encoding='utf-8')
    return {s: len(v) for s, v in d.items()}

def split_ssc():
    d = node_eval(f"global.window={{}};require('./ssc-{C}.js');const w=window;process.stdout.write(JSON.stringify({{q:w.RAAY_SSC[{C}],mm:w.RAAY_MM,bm:w.RAAY_SSC_BM,ln:w.RAAY_SSC_LN}}))")
    for s, items in d['q'].items():
        (R / f'ssc-{C}-{s}.js').write_text(
            f"/* {C}వ తరగతి SSC – {s} ప్రశ్నలు (tools/split/split_class10.py) */\n"
            f"((window.RAAY_SSC=window.RAAY_SSC||{{}})[{C}]=window.RAAY_SSC[{C}]||{{}})[{json.dumps(s)}]={dump(items)};\n", encoding='utf-8')
    head = [f"/* {C}వ తరగతి SSC సూచిక – ప్రశ్నలు ssc-{C}-<సబ్జెక్టు>.js నుండి అవసరమైనప్పుడు (tools/split/split_class10.py) */",
            f"(window.RAAY_SSC=window.RAAY_SSC||{{}})[{C}]=window.RAAY_SSC[{C}]||{{}};",
            f"(window.RAAY_SSC_N=window.RAAY_SSC_N||{{}})[{C}]={dump({s: len(v) for s, v in d['q'].items()})};"]
    for k, var in (('mm', 'RAAY_MM'), ('bm', 'RAAY_SSC_BM'), ('ln', 'RAAY_SSC_LN')):
        if d.get(k) is not None: head.append(f"window.{var}={dump(d[k])};")
    (R / f'ssc-{C}-idx.js').write_text('\n'.join(head) + '\n', encoding='utf-8')
    return {s: len(v) for s, v in d['q'].items()}

if __name__ == '__main__':
    print('notes', split_notes())
    print('ssc', split_ssc())
