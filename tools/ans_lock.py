# జవాబుల దాపరికం (2026-11-12): answers-*.js లోని జవాబులు + notes-*.js లోని టీచర్ గైడ్ (tg) జవాబులు
# ఫైల్ నేరుగా తెరిస్తే చదవలేని రూపంలోకి. యాప్ `unz()` తో తిరిగి తెలుగులోకి మారుస్తుంది.
# రూపం: "⁂" + ప్రతి అక్షరం (U+CFF0 లోపు) +7 షిఫ్ట్. JSON ఆకారం మారదు → build స్క్రిప్టులు అలాగే పనిచేస్తాయి;
# అవి కొత్తగా రాసే సాదా జవాబులను ఈ స్క్రిప్ట్ మళ్ళీ నడిపితే దాస్తుంది (ఇప్పటికే దాచినవి మారవు – idempotent).
# ⚠️ ఏ build (build6/7/8/9, build_lang, import_data, split_class10) నడిపినా తర్వాత: python3 tools/ans_lock.py
# చదవడానికి (డీబగ్): python3 tools/ans_lock.py --show "⁂..."
# 100% రక్షణ కాదు – సాధారణంగా లింక్ తెరిచే విద్యార్థి చదవలేడు. మూల ch/*.py ఫైళ్లు repo లో సాదాగానే ఉంటాయి.
import json, re, sys, glob, os

M = '⁂'
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def z(s):
    if not isinstance(s, str) or s.startswith(M) or not s:
        return s
    return M + ''.join(chr(ord(c) + 7) if ord(c) < 0xCFF0 else c for c in s)


def unz(s):
    if not isinstance(s, str) or not s.startswith(M):
        return s
    return ''.join(chr(ord(c) - 7) if 7 <= ord(c) < 0xCFF7 else c for c in s[1:])


def lock_ans(o):  # {file:{page:[str]}}
    n = 0
    for f in o.values():
        if isinstance(f, dict):
            for p, arr in f.items():
                if isinstance(arr, list):
                    for i, s in enumerate(arr):
                        t = z(s)
                        if t is not s:
                            arr[i] = t; n += 1
    return n


def lock_tg(o):  # ఏ dict లో 'tg' ఉన్నా [[శీర్షిక,[జవాబులు]]]
    n = 0
    if isinstance(o, dict):
        tg = o.get('tg')
        if isinstance(tg, list):
            for sec in tg:
                if isinstance(sec, list) and len(sec) > 1 and isinstance(sec[1], list):
                    for i, s in enumerate(sec[1]):
                        t = z(s)
                        if t is not s:
                            sec[1][i] = t; n += 1
        for v in o.values():
            n += lock_tg(v)
    elif isinstance(o, list):
        for v in o:
            n += lock_tg(v)
    return n


def process(path, fn):
    src = open(path, encoding='utf-8').read()
    out, pos, n = [], 0, 0
    dec = json.JSONDecoder()
    for m in re.finditer(r'\]=(?=[\[{])', src):
        st = m.end()
        if st < pos:
            continue
        obj, end = dec.raw_decode(src, st)
        k = fn(obj)
        n += k
        out.append(src[pos:st]); out.append(json.dumps(obj, ensure_ascii=False, separators=(',', ':')) if k else src[st:end])
        pos = end
    out.append(src[pos:])
    if n:
        open(path, 'w', encoding='utf-8').write(''.join(out))
    return n


if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == '--show':
        print(unz(sys.argv[2])); sys.exit()
    tot = 0
    for p in sorted(glob.glob(f'{REPO}/answers-*.js')):
        k = process(p, lock_ans); tot += k
        if k: print('🔐', os.path.basename(p), k)
    for p in sorted(glob.glob(f'{REPO}/notes-*.js')):
        k = process(p, lock_tg); tot += k
        if k: print('🔐', os.path.basename(p), 'tg', k)
    print('మొత్తం కొత్తగా దాచినవి:', tot)
