"""ఆటల పటాలు → games-maps.js (window.RAAY_MAPS).
మూలం: npm @svg-maps/india, @svg-maps/world 2.0.0 (CC BY 4.0, VictorCazanave/svg-maps) – `npm pack` చేసి ఈ ఫోల్డర్ పక్కన విప్పాలి:
  cd /tmp/mp && npm pack @svg-maps/india @svg-maps/world && tar xzf ... (ఫోల్డర్లు svg-maps-india-2.0.0, svg-maps-world-2.0.0)
వాడకం: python3 tools/games_maps/build_maps.py /tmp/mp games-maps.js
భారత పటం: రాష్ట్రాల వారీ (1 దశాంశం, సరళీకరణ). ప్రపంచ పటం: దేశాల సరిహద్దులు లేకుండా ఖండాల వారీగా కలిపి (shapely union) – దేశాల ఆకారాలు చూపము.
"""
import sys, json
from svgpathtools import parse_path
from shapely.geometry import Polygon, MultiPolygon
from shapely.ops import unary_union
import pycountry_convert as pc

src, out = sys.argv[1], sys.argv[2]

def load(f):
    s = open(f, encoding='utf-8').read()
    return json.loads(s[s.index('{'):s.rindex('}') + 1])

def polys(d, step=1.0):
    P = parse_path(d); res = []
    for sp in P.continuous_subpaths():
        pts = []
        for seg in sp:
            n = max(1, int(seg.length() / step)) if seg.length() > 0 else 1
            for k in range(n):
                z = seg.point(k / n); pts.append((z.real, z.imag))
        if len(pts) >= 3:
            g = Polygon(pts).buffer(0)
            if not g.is_empty: res.append(g)
    return unary_union(res) if res else None

def to_d(g, tol, minA):
    g = g.simplify(tol, preserve_topology=True)
    gs = list(g.geoms) if isinstance(g, MultiPolygon) else [g]
    out = []
    for p in gs:
        if p.area < minA: continue
        for ring in [p.exterior] + list(p.interiors):
            c = list(ring.coords)[:-1]
            if len(c) < 3: continue
            out.append('M' + 'L'.join(f'{x:.1f} {y:.1f}' for x, y in c) + 'Z')
    return ''.join(out)

ind = load(f'{src}/svg-maps-india-2.0.0/index.js')
I = {}
for l in ind['locations']:
    g = polys(l['path'], 1.5)
    if g is None: continue
    d = to_d(g, 0.6, 0.3 if l['id'] in ('an', 'ld') else 2)
    if d: I[l['id']] = d

wd = load(f'{src}/svg-maps-world-2.0.0/index.js')
cont = {}
for l in wd['locations']:
    iso = l['id'].upper()
    try: cc = pc.country_alpha2_to_continent_code(iso)
    except Exception:
        cc = {'AQ': 'AN', 'TL': 'AS', 'EH': 'AF', 'SX': 'NA', 'XK': 'EU', 'BQ': 'NA', 'UM': 'OC', 'TF': 'AN', 'PN': 'OC', 'VA': 'EU'}.get(iso)
    if not cc: print('skip', iso, l['name']); continue
    g = polys(l['path'], 3)
    if g is None: continue
    if iso == 'RU':  # రష్యా: ఉరల్ పర్వతాలు (~60° తూ.రే.) పడమర యూరప్, తూర్పు ఆసియా (బడి పుస్తకాల ప్రకారం)
        from shapely.geometry import box
        X = 668
        cont.setdefault('EU', []).append(g.intersection(box(-50, -50, X, 700)))
        cont.setdefault('AS', []).append(g.intersection(box(X, -50, 1100, 700)))
        continue
    cont.setdefault(cc, []).append(g)
W = {}
for cc, gs in cont.items():
    u = unary_union([g.buffer(0.8) for g in gs]).buffer(-0.8)
    W[cc] = to_d(u, 1.2, 6)
js = ('/* ఆటల పటాలు – మూలం @svg-maps/india, @svg-maps/world (CC BY 4.0, VictorCazanave/svg-maps); tools/games_maps/build_maps.py */\n'
      'window.RAAY_MAPS=' + json.dumps({'in': {'vb': ind['viewBox'], 'p': I}, 'w': {'vb': wd['viewBox'], 'p': W}}, ensure_ascii=False, separators=(',', ':')) + ';\n')
open(out, 'w', encoding='utf-8').write(js)
print('ok', len(js) // 1024, 'KB', len(I), 'states', sorted(W))
