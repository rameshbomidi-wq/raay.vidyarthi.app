# 🔐 జవాబుల తాళం (v2, 2026-11-12): answers-*.js పేజీ జవాబులు + notes-*.js టీచర్ గైడ్ (tg) → AES-256-GCM గూఢలిపి.
# తాళం చెవి = HMAC-SHA256(AKS, label). AKS రహస్యం – repo లో ఎప్పుడూ పెట్టకూడదు:
#   env AKS లేదా tools/.aks ఫైల్ (.gitignore లో) లేదా ఈ స్క్రిప్ట్ పక్కన ../../aks/AKS.txt.
#   అదే AKS పబ్లిక్ సర్వర్ Apps Script → Project Settings → Script Properties → AKS లో ఉండాలి (ping లో akh = sha256(AKS)[:8]).
# label: పేజీ ఏ పాఠానికి చెందితే "c|sub|lessonId" (టీచర్ ఆ పాఠం/పుస్తకం 🔓 తెరిస్తే పిల్లలకు సర్వర్ key ఇస్తుంది);
#        ఏ పాఠానికీ చెందని పేజీ "T|c|file"; టీచర్ గైడ్ "T|c|lessonId|tg" (టీచర్లకు మాత్రమే).
# పేజీ → పాఠం: యాప్ ansLessonOf లాగే (learnSubs క్రమం, akRange = wb.p .. wb.p + (pg రెండో సంఖ్య − మొదటిది)).
# ⚠️ ఏ build/import/split నడిపినా తర్వాత: python3 tools/ans_lock.py  (ఇప్పటికే గూఢలిపిలో ఉన్నవి మారవు – idempotent)
# పరీక్ష: python3 tools/ans_lock.py --check  (ప్రతి తరగతి నుండి కొన్ని తెరిచి చూపిస్తుంది)
import json, re, sys, glob, os, hmac, hashlib, base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M = '⁂'


def secret():
    s = os.environ.get('AKS', '')
    for f in (os.path.join(REPO, 'tools', '.aks'), os.path.join(os.path.dirname(REPO), 'aks', 'AKS.txt')):
        if not s and os.path.exists(f):
            s = open(f).read().strip()
    if not s:
        sys.exit('AKS రహస్యం దొరకలేదు (env AKS / tools/.aks)')
    return s


SEC = None


def key(label):
    return hmac.new(SEC.encode(), label.encode(), hashlib.sha256).digest()


def enc(label, obj):
    iv = os.urandom(12)
    ct = AESGCM(key(label)).encrypt(iv, json.dumps(obj, ensure_ascii=False).encode(), None)
    return {'l': label, 'e': base64.b64encode(iv + ct).decode()}


def dec(o):
    d = base64.b64decode(o['e'])
    return json.loads(AESGCM(key(o['l'])).decrypt(d[:12], d[12:], None))


def unz(s):
    if not isinstance(s, str) or not s.startswith(M):
        return s
    return ''.join(chr(ord(c) - 7) if 7 <= ord(c) < 0xCFF7 else c for c in s[1:])


def subjects_for(c):
    return ['tel', 'eng', 'mat'] if c <= 2 else ['tel', 'eng', 'mat', 'evs'] if c <= 5 else ['tel', 'hin', 'eng', 'mat', 'sci', 'soc'] if c <= 7 else ['tel', 'hin', 'eng', 'mat', 'phy', 'bio', 'soc']


def learn_subs(c):
    a = subjects_for(c)
    return a + ['te2'] if c >= 6 else a


def objs(src):
    """'...]=' తర్వాత ఉన్న ప్రతి JSON (స్థానం, వస్తువు, ముగింపు)"""
    dec_ = json.JSONDecoder()
    pos = 0
    for m in re.finditer(r'\]=(?=[\[{])', src):
        st = m.end()
        if st < pos:
            continue
        o, end = dec_.raw_decode(src, st)
        yield st, o, end
        pos = end


def rewrite(path, fn):
    src = open(path, encoding='utf-8').read()
    out, pos, n = [], 0, 0
    for st, o, end in objs(src):
        k = fn(o)
        n += k
        out.append(src[pos:st])
        out.append(json.dumps(o, ensure_ascii=False, separators=(',', ':')) if k else src[st:end])
        pos = end
    out.append(src[pos:])
    if n:
        open(path, 'w', encoding='utf-8').write(''.join(out))
    return n


def page_map(c):
    """{(file, page): 'c|sub|lid'} – ansLessonOf క్రమంలో మొదటిది"""
    p = os.path.join(REPO, f'notes-{c}.js')
    if not os.path.exists(p):
        return {}
    tb = {}
    for _, o, _ in objs(open(p, encoding='utf-8').read()):
        if isinstance(o, dict):
            tb.update(o)
    mp = {}
    for s in learn_subs(c):
        for L in tb.get(s, []) or []:
            W = L.get('wb') or {}
            if not W.get('f'):
                continue
            a = int(W.get('p') or 1)
            m = re.search(r'(\d+)\D+(\d+)', str(W.get('pg') or ''))
            b = a + (int(m.group(2)) - int(m.group(1))) if m else a
            f = str(W['f']).split('/')[-1]
            for pg in range(a, b + 1):
                mp.setdefault((f, str(pg)), f'{c}|{s}|{L["id"]}')
    return mp


def lock_ans(c):
    mp = page_map(c)

    def fn(o):
        n = 0
        for f, pages in o.items():
            if not isinstance(pages, dict):
                continue
            for pg, v in list(pages.items()):
                if isinstance(v, list):
                    pages[pg] = enc(mp.get((f, str(pg)), f'T|{c}|{f}'), [unz(x) for x in v])
                    n += 1
        return n
    return fn


def lock_tg(c):
    def walk(o):
        n = 0
        if isinstance(o, dict):
            if isinstance(o.get('tg'), list) and o.get('id'):
                tg = [[g[0], [unz(x) for x in g[1]]] if isinstance(g, list) and len(g) > 1 and isinstance(g[1], list) else g for g in o['tg']]
                o['tg'] = enc(f'T|{c}|{o["id"]}|tg', tg)
                n += 1
            for v in o.values():
                n += walk(v)
        elif isinstance(o, list):
            for v in o:
                n += walk(v)
        return n
    return walk


def cls_of(path):
    return int(re.match(r'(?:answers|notes)-(\d+)', os.path.basename(path)).group(1))


if __name__ == '__main__':
    SEC = secret()
    print('akh', hashlib.sha256(SEC.encode()).hexdigest()[:8])
    if '--check' in sys.argv:
        for p in sorted(glob.glob(f'{REPO}/answers-*.js')):
            for _, o, _ in objs(open(p, encoding='utf-8').read()):
                f = next(iter(o)); pg = next(iter(o[f])); v = o[f][pg]
                print(os.path.basename(p), v['l'] if isinstance(v, dict) else 'PLAIN', str(dec(v) if isinstance(v, dict) else v)[:70])
        sys.exit()
    tot = 0
    for p in sorted(glob.glob(f'{REPO}/answers-*.js')):
        k = rewrite(p, lock_ans(cls_of(p))); tot += k
        if k: print('🔐', os.path.basename(p), k)
    for p in sorted(glob.glob(f'{REPO}/notes-*.js')):
        k = rewrite(p, lock_tg(cls_of(p))); tot += k
        if k: print('🔐', os.path.basename(p), 'tg', k)
    print('మొత్తం కొత్తగా గూఢలిపిలోకి:', tot)
