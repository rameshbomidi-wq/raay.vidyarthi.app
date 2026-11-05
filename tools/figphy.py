"""భౌతిక శాస్త్రం కిరణ చిత్రాలు (ray diagrams) – figlib SVG టోకెన్లతో, సూత్రాలతో ఖచ్చితంగా లెక్కించి గీస్తుంది.
mirror('cc'|'cx', u)  – పుటాకార/కుంభాకార దర్పణం, u = వస్తువు దూరం F యూనిట్లలో (ఉదా: 3 = C కి ఆవల, 2 = C వద్ద, 'inf' = అనంతం)
lens('cv'|'cc', u)    – కుంభాకార/పుటాకార కటకం
"""
from figlib import F, S, T, PG, P, ARC
import math

FU = 2.0   # ఒక F = 2 యూనిట్లు
H = 1.4    # వస్తువు ఎత్తు

def _ray(x1, y1, x2, y2, st='1', mid=True):
    """బాణంతో కిరణం (మధ్యలో దిశ బాణం)"""
    if not mid: return [S(x1, y1, x2, y2, st)]
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    return [S(x1, y1, mx, my, st + 'a'), S(mx, my, x2, y2, st)]

def _clip(x0, y0, dx, dy, xe):
    """(x0,y0) నుండి (dx,dy) దిశలో x = xe వరకు"""
    t = (xe - x0) / dx if abs(dx) > 1e-9 else 0
    return x0 + dx * t, y0 + dy * t

def _view(xs, ys, pad=0.8):
    return [min(xs) - pad, max(xs) + pad, min(ys) - pad, max(ys) + pad]

def _arrow(x, h, st='b'):
    return S(x, 0, x, h, st + 'a')

def mirror(kind, u, cap='', w=330):
    """కిరణ చిత్రం – దర్పణం P = (0,0); వస్తువు ఎడమ వైపు."""
    f = -FU if kind == 'cc' else FU          # కార్టీసియన్ గుర్తుల పద్ధతి
    e, lab = [], []
    ym = 2.6
    # దర్పణం: పుటాకారం = అంచులు ఎడమకు వంగుతాయి
    sag = 0.35 if kind == 'cc' else -0.35
    pts = [[-sag * (y / ym) ** 2, y] for y in [ym * (i / 10 - 1) for i in range(21)]]
    for a, b in zip(pts, pts[1:]): e.append(S(a[0], a[1], b[0], b[1], 'b'))
    for y in [ym * (i / 6 - 1) for i in range(13)]:   # వెనుక గీతలు (hatching)
        x = -sag * (y / ym) ** 2
        e.append(S(x, y, x + 0.25, y + 0.2, ''))
    if u == 'inf':
        xs = [-3.4 * FU, 0.6]; ys = [-ym, ym]
        for y in (1.2, 0.0, -1.2):
            e += _ray(-3.2 * FU, y, 0, y)
            if not y: continue
            if kind == 'cc':
                x2 = f * 1.7; e += _ray(0, y, x2, y * (1 - x2 / f), '1')
            else:
                x2 = -2.2; e += _ray(0, y, x2, y * (1 - x2 / f), '1'); e.append(S(0, y, f, 0, '1d'))
        e.append(P(f, 0, '', 'n', '2'))
    else:
        uu = -u * FU
        v = 1 / (1 / f - 1 / uu) if abs(1 / f - 1 / uu) > 1e-9 else None
        e.append(_arrow(uu, H)); e.append(T(uu, H + 0.3, 'వస్తువు', 'middle', 10))
        xs, ys = [uu, 0.6, -2 * FU - 0.3], [-ym, ym, H]
        # కిరణం 1: అక్షానికి సమాంతరం → F గుండా (లేదా F నుండి వచ్చినట్లు)
        e += _ray(uu, H, 0, H)
        # కిరణం 2: P వద్దకు → సమాన కోణంతో పరావర్తనం
        e += _ray(uu, H, 0, 0)
        if v is None:   # వస్తువు F వద్ద – సమాంతర కిరణాలు
            x2 = uu - 1.2
            e += _ray(0, H, x2, H + (-H / f) * x2, '1')
            e += _ray(0, 0, x2, -H * x2 / uu, '1')
            img = 'అనంతం వద్ద'
        else:
            hi = -v / uu * H
            real = v < 0
            if real:
                # కిరణం 1 F గుండా ప్రతిబింబం వరకు, కొంచెం ముందుకు
                d = (v - 0) * 1.12
                e += _ray(0, H, d, H + (hi - H) * 1.12, '1')
                e += _ray(0, 0, d, hi * 1.12, '1')
                e.append(_arrow(v, hi, '2b')); e.append(T(v, hi + (0.3 if hi > 0 else -0.45), 'ప్రతిబింబం', 'middle', 10, '2'))
                xs += [v * 1.12]; ys += [hi * 1.12]
            else:
                # పరావర్తిత కిరణాలు ఎడమకు; వెనుక చుక్కల పొడిగింపు ప్రతిబింబం వరకు
                x2 = uu * 0.9
                e += _ray(0, H, x2, H + (hi - H) / v * x2, '1')
                e += _ray(0, 0, x2, hi / v * x2, '1')
                e.append(S(0, H, v, hi, '1d')); e.append(S(0, 0, v, hi, '1d'))
                e.append(S(v, 0, v, hi, '2bda')); e.append(T(v, hi + 0.3, 'ప్రతిబింబం', 'middle', 10, '2'))
                xs += [v + 0.4, x2]; ys += [hi, H + (hi - H) / v * x2]
            img = (v, hi, real)
    # అక్షం, లేబుళ్లు
    v0 = _view(xs, ys)
    v0[0] = min(v0[0], -2 * FU - 0.8) if kind == 'cc' else v0[0]
    v0[1] = max(v0[1], 2 * FU + 0.8) if kind == 'cx' else v0[1]
    e.insert(0, S(v0[0] + 0.1, 0, v0[1] - 0.1, 0, ''))
    for x, t in ((0, 'P'), (f, 'F'), (2 * f, 'C')):
        if v0[0] < x < v0[1]:
            e.append(P(x, 0, '', 'n')); e.append(T(x + (0.25 if x == 0 else 0), -0.5, t, 'middle', 12, None, 1))
    if not cap: cap = ('పుటాకార' if kind == 'cc' else 'కుంభాకార') + ' దర్పణం'
    return F(v0, *e, w=w, cap=cap, al=cap)

def lens(kind, u, cap='', w=340):
    """కిరణ చిత్రం – కటకం O = (0,0); వస్తువు ఎడమ వైపు (F1, 2F1)."""
    f = FU if kind == 'cv' else -FU
    e = []
    ym = 2.6
    # కటకం ఆకారం
    n = 16
    if kind == 'cv':
        R = [[0.35 * math.cos(math.pi / 2 * (i / n * 2 - 1)), ym * (i / n * 2 - 1)] for i in range(n + 1)]
        pts = R + [[-p[0], p[1]] for p in reversed(R)]
    else:
        R = [[0.12 + 0.3 * (1 - math.cos(math.pi / 2 * (i / n * 2 - 1))), ym * (i / n * 2 - 1)] for i in range(n + 1)]
        pts = R + [[-p[0], p[1]] for p in reversed(R)]
    e.append(PG([[round(a, 3), round(b, 3)] for a, b in pts], '#dbeafe', '#1e3a8a'))
    if u == 'inf':
        xs, ys = [-3.2 * FU, 3.2 * FU], [-ym, ym]
        for y in (1.3, 0.0, -1.3):
            e += _ray(-3 * FU, y, 0, y)
            if kind == 'cv':
                if y: e += _ray(0, y, f * 1.6, y - y / f * f * 1.6, '1')
                else: e += _ray(0, 0, f * 1.6, 0, '1')
            else:
                if y:
                    e += _ray(0, y, 2.4, y + y / FU * 2.4, '1'); e.append(S(0, y, f, 0, '1d'))
                else: e += _ray(0, 0, 2.6, 0, '1')
        e.append(P(f, 0, '', 'n', '2'))
    else:
        uu = -u * FU
        den = 1 / f + 1 / uu
        v = 1 / den if abs(den) > 1e-9 else None
        e.append(_arrow(uu, H)); e.append(T(uu, H + 0.3, 'వస్తువు', 'middle', 10))
        xs, ys = [uu, -2 * FU - 0.3, 2 * FU + 0.3], [-ym, ym, H]
        e += _ray(uu, H, 0, H)            # సమాంతర కిరణం
        e += _ray(uu, H, 0, 0)            # దృక్ కేంద్రం గుండా
        if v is None:
            x2 = 2 * FU
            e += _ray(0, H, x2, H - H / f * x2, '1'); e += _ray(0, 0, x2, -H / uu * x2, '1')
        else:
            hi = v / uu * H
            if v > 0:
                d = v * 1.12
                e += _ray(0, H, d, H + (hi - H) * 1.12, '1'); e += _ray(0, 0, d, hi * 1.12, '1')
                e.append(_arrow(v, hi, '2b')); e.append(T(v, hi + (0.3 if hi > 0 else -0.45), 'ప్రతిబింబం', 'middle', 10, '2')); xs += [d]; ys += [hi * 1.12]
            else:
                x2 = 1.5 * FU
                e += _ray(0, H, x2, H + (H - hi) / (0 - v) * x2, '1'); e += _ray(0, 0, x2, hi / v * x2, '1')
                e.append(S(0, H, v, hi, '1d')); e.append(S(0, 0, v, hi, '1d'))
                e.append(S(v, 0, v, hi, '2bda')); e.append(T(v, hi + 0.3, 'ప్రతిబింబం', 'middle', 10, '2')); xs += [x2, v]; ys += [hi, H + (H - hi) / (0 - v) * x2]
    v0 = _view(xs, ys)
    e.insert(0, S(v0[0] + 0.1, 0, v0[1] - 0.1, 0, ''))
    for x, t in ((0, 'O'), (-FU, 'F₁'), (-2 * FU, '2F₁'), (FU, 'F₂'), (2 * FU, '2F₂')):
        if v0[0] < x < v0[1]:
            e.append(P(x, 0, '', 'n')); e.append(T(x + (0.3 if x == 0 else 0), -0.5, t, 'middle', 11, None, 1))
    if not cap: cap = ('కుంభాకార' if kind == 'cv' else 'పుటాకార') + ' కటకం'
    return F(v0, *e, w=w, cap=cap, al=cap)

# ── విద్యుత్ వలయ పటాలు ──
from figlib import C as _C

def _res(x1, y, x2, lb=''):
    """క్షితిజ నిరోధం (జిగ్‌జాగ్) x1→x2 వద్ద"""
    e, n, w = [], 6, (x2 - x1)
    pts = [(x1, y)] + [(x1 + w * (i + 0.5) / n, y + (0.22 if i % 2 == 0 else -0.22)) for i in range(n)] + [(x2, y)]
    for a, b in zip(pts, pts[1:]): e.append(S(a[0], a[1], b[0], b[1], 'b'))
    if lb: e.append(T((x1 + x2) / 2, y + 0.45, lb, 'middle', 12, '2', 1))
    return e

def _cells(x, y, n):
    """బ్యాటరీ – n ఘటాలు (పొడవాటి = +, పొట్టి = –); x నుండి కుడికి"""
    e = []
    for i in range(n):
        cx = x + i * 0.4
        e.append(S(cx, y - 0.4, cx, y + 0.4, 'b')); e.append(S(cx + 0.18, y - 0.2, cx + 0.18, y + 0.2, 'b'))
        if i < n - 1: e.append(S(cx + 0.18, y, cx + 0.4, y, ''))
    e.append(T(x - 0.15, y + 0.55, '+', 'middle', 12)); e.append(T(x + (n - 1) * 0.4 + 0.35, y + 0.55, '–', 'middle', 12))
    return e, x + (n - 1) * 0.4 + 0.18

def _meter(x, y, t):
    return [_C(x, y, 0.32, '', '#fff'), T(x, y - 0.13, t, 'middle', 12, None, 1)]

def _key(x, y):
    return [_C(x, y, 0.22, '', '#fff'), P(x, y, '', 'n'), T(x, y + 0.45, 'K', 'middle', 11)]

def series_circ(cells=2, nres=2, volt=False, cap='శ్రేణి వలయం', w=320):
    e = []
    W = 2.2 * nres + 1.6
    # పై తీగ – నిరోధాలు
    x = 0.8; e.append(S(0, 4, x, 4))
    for i in range(nres):
        e += _res(x, 4, x + 1.8, 'R' + '₁₂₃₄'[i]); x += 1.8
        nx = x + 0.4 if i < nres - 1 else W
        e.append(S(x, 4, nx, 4)); x = nx
    e.append(S(W, 4, W, 0))
    # కింది తీగ: బ్యాటరీ, కీ
    bx = W * 0.25; ce, bx2 = _cells(bx, 0, cells)
    e += [S(0, 0, bx, 0), S(bx2, 0, W * 0.7 - 0.22, 0), S(W * 0.7 + 0.22, 0, W, 0)] + ce + _key(W * 0.7, 0)
    # ఎడమ తీగ: అమ్మీటర్
    e += [S(0, 0, 0, 1.68), S(0, 2.32, 0, 4)] + _meter(0, 2, 'A')
    if volt:
        e += [S(0.8, 4, 0.8, 3.0), S(x - 0.4 if nres else 2.6, 4, x - 0.4, 3.0)]
        xv = (0.8 + x - 0.4) / 2
        e += [S(0.8, 3.0, xv - 0.32, 3.0), S(xv + 0.32, 3.0, x - 0.4, 3.0)] + _meter(xv, 3.0, 'V')
    e.append(T(W + 0.15, 2, 'I ↓', 'start', 11))
    return F([-0.8, W + 0.9, -0.9, 4.9], *e, w=w, cap=cap, al=cap)

def parallel_circ(cells=3, nres=2, cap='సమాంతర వలయం', w=320):
    e = []
    W = 6.0
    ys = [4.6 - i * 1.0 for i in range(nres)]
    # X, Y జంక్షన్లు
    e += [S(0, 4, 1.4, 4), S(W - 1.4, 4, W, 4)]
    e += [S(1.4, max(ys), 1.4, min(ys)), S(W - 1.4, max(ys), W - 1.4, min(ys))]
    for i, y in enumerate(ys):
        e += [S(1.4, y, 2.1, y), S(W - 2.1, y, W - 1.4, y)] + _res(2.1, y, W - 2.1, 'R' + '₁₂₃₄'[i])
    e += [P(1.4, 4, 'X', 'w'), P(W - 1.4, 4, 'Y', 'e')]
    e.append(S(W, 4, W, 0))
    bx = 1.2; ce, bx2 = _cells(bx, 0, cells)
    e += [S(0, 0, bx, 0), S(bx2, 0, W * 0.72 - 0.22, 0), S(W * 0.72 + 0.22, 0, W, 0)] + ce + _key(W * 0.72, 0)
    e += [S(0, 0, 0, 1.68), S(0, 2.32, 0, 4)] + _meter(0, 2, 'A')
    return F([-0.8, W + 0.6, -0.9, max(ys) + 0.9], *e, w=w, cap=cap, al=cap)
