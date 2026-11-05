"""రాయ్ విద్యార్థి – బొమ్మల (SVG) టోకెన్ తయారీ. యాప్‌లో richT()/figSVG() వీటిని గీస్తాయి.
F(v, *elements, g=1 గ్రాఫ్ కాగితం, ax=1 అక్షాలు మాత్రమే, w=వెడల్పు px, st=గ్రిడ్ అడుగు, n=సంఖ్యల అడుగు, cap=శీర్షిక)
v = [xmin, xmax, ymin, ymax] (గణిత నిరూపకాలు, y పైకి). రంగులు: st లో '1'..'5' (నీలం, ఎరుపు, ఆకుపచ్చ, ఊదా, నారింజ).
"""
import json, math

def F(v, *e, g=0, ax=0, w=300, st=None, n=None, cap=None, al=None, nt=None, xl=None, yl=None):
    o = {'v': [round(x, 3) for x in v], 'w': w, 'e': [_r(list(x)) for x in e if x]}
    for k, val in (('g', g), ('ax', ax), ('st', st), ('n', n), ('cap', cap), ('al', al), ('nt', nt), ('xl', xl), ('yl', yl)):
        if val not in (None, 0, '') or (k == 'nt' and val == 0 and nt is not None):
            o[k] = val
    return '⟦fig:' + json.dumps(o, ensure_ascii=False, separators=(',', ':')) + '⟧'

def _r(a):
    out = []
    for x in a:
        if isinstance(x, float): x = round(x, 3)
        elif isinstance(x, list): x = _r(x)
        out.append(x)
    while out and out[-1] is None: out.pop()
    return out

# మూలకాలు
def P(x, y, lb='', pos='ne', st=None): return ['p', x, y, lb, pos, st]                      # బిందువు
def S(x1, y1, x2, y2, st=''): return ['s', x1, y1, x2, y2, st]                                 # రేఖాఖండం (d=చుక్కలు, a=బాణం, A=రెండువైపులా, b=మందం, అంకె=రంగు)
def L(a, b, c, lb='', lx=None, ly=None, st=None): return ['l', a, b, c, lb, lx, ly, st]        # ax + by + c = 0
def FN(ex, lb='', x0=None, x1=None, lx=None, ly=None, st=None): return ['f', ex, lb, x0, x1, lx, ly, st]  # y = f(x) (JS)
def PG(pts, fill=None, stroke=None): return ['pg', pts, fill, stroke]                         # బహుభుజి
def C(x, y, r, st='', fill=None): return ['c', x, y, r, st, fill]                             # వృత్తం
def A(x, y, r, a1, a2, lb='', st=None, off=None): return ['a', x, y, r, a1, a2, lb, st, off]  # కోణం గుర్తు (డిగ్రీలు, అపసవ్య దిశ)
def R(x, y, a1, a2, z=None): return ['r', x, y, a1, a2, z]                                    # లంబకోణం గుర్తు
def M(x1, y1, x2, y2, lb, sd=1, st=None): return ['m', x1, y1, x2, y2, lb, sd, st]            # భుజం కొలత (sd = ±1 వైపు)
def T(x, y, t, anchor='middle', sz=12, st=None, b=None): return ['t', x, y, t, anchor, sz, st, b]  # పాఠ్యం

def ang(x1, y1, x2, y2):
    """(x1,y1) నుండి (x2,y2) దిశ కోణం (డిగ్రీలు)"""
    return math.degrees(math.atan2(y2 - y1, x2 - x1))

def ARC(x, y, rx, ry, a1, a2, st='', fill=None): return ['arc', x, y, rx, ry, a1, a2, st, fill]  # దీర్ఘవృత్త/వృత్త చాపం (నమూనాలతో)
def EL(x, y, rx, ry, st='', back_dashed=False):
    """దీర్ఘవృత్తం; back_dashed=True అయితే వెనుక (పై) సగం చుక్కలు – 3D ఘనాకృతులకు"""
    if back_dashed: return [ARC(x, y, rx, ry, 180, 360, st), ARC(x, y, rx, ry, 0, 180, (st or '') + 'd')]
    return [ARC(x, y, rx, ry, 0, 360, st)]
def SECTOR(x, y, r, a1, a2, fill='#fde68a', stroke='#1f2937'):
    pts = [[x, y]] + [[round(x + r * math.cos(math.radians(a1 + (a2 - a1) * i / 30)), 3), round(y + r * math.sin(math.radians(a1 + (a2 - a1) * i / 30)), 3)] for i in range(31)]
    return PG(pts, fill, stroke)
def line_lbl(a, b, c, v, frac):
    """ax+by+c=0 రేఖపై లేబుల్ స్థానం (వీక్షణలో frac భాగం వద్ద)"""
    x = v[0] + (v[1] - v[0]) * frac
    if abs(b) < 1e-9: return (-c / a + 0.3, v[2] + (v[3] - v[2]) * frac)
    y = (-c - a * x) / b
    if y > v[3] - 0.4 or y < v[2] + 0.4:
        y = v[3] - (v[3] - v[2]) * 0.08 if y > v[3] - 0.4 else v[2] + (v[3] - v[2]) * 0.08
        x = (-c - b * y) / a if abs(a) > 1e-9 else x
    return (round(x, 2), round(y + (v[3] - v[2]) * 0.04, 2))
