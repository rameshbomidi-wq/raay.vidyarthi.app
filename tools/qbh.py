"""భాషా ప్రశ్నల బ్యాంక్ సహాయకం: Q(tag, lid, mk, ప్రశ్న, జవాబు, తప్పు_ఎంపికలు=None, వివరణ='') → 10-ఫీల్డ్ tuple (English లేదు)."""
def Q(tag, lid, mk, q, a, w=None, ex=''):
    return (tag, lid, mk, q, a, '', '', list(w) if w else None, ex, '')
def MCQ(tag, lid, q, opts, k, ex=''):
    """opts = [అ, ఆ, ఇ, ఈ] ఎంపికలు; k = సరైనది సూచిక (0–3)"""
    return Q(tag, lid, 1, q, opts[k], [o for i, o in enumerate(opts) if i != k], ex)

class Bank:
    """ఒక పాఠం ప్రశ్నలు – tag ఆటో: QB<L>-<pre><ch>-<mk>-<క్రమసంఖ్య>"""
    def __init__(self, ch, lid, pre=''):
        self.ch, self.lid, self.pre, self.n, self.items = ch, lid, pre, {}, []
    def _t(self, L, mk):
        k = (L, mk); self.n[k] = self.n.get(k, 0) + 1
        return f'QB{L}-{self.pre}{self.ch:02d}-{mk}-{self.n[k]}'
    def q(self, L, mk, q, a, w=None, ex='', lid=None):
        self.items.append(Q(self._t(L, mk), lid or self.lid, mk, q, a, w, ex)); return self
    def mcq(self, L, q, opts, k, ex='', mk=1, lid=None):
        self.items.append(Q(self._t(L, mk), lid or self.lid, mk, q, opts[k], [o for i, o in enumerate(opts) if i != k], ex)); return self

# తెలుగు భాషాంశాల ప్రశ్న తోకలు
AR, PY, PV, NN, SD, SM, VY = 'పదానికి అర్థం రాయండి.', 'పదానికి పర్యాయపదాలు రాయండి.', 'పదానికి ప్రకృతి / వికృతి రాయండి.', 'పదానికి నానార్థాలు రాయండి.', 'పదాన్ని విడదీసి, సంధి పేరు రాయండి.', 'పదానికి విగ్రహవాక్యం రాసి, సమాసం పేరు రాయండి.', 'పదానికి వ్యుత్పత్త్యర్థం రాయండి.'

# English బ్యాంక్: PDF నుండి తీసిన పేజీ పాఠ్యం (src_pages.json) లోని వరుసలను ప్రశ్నగా వాడటం – మళ్ళీ టైప్ చేయనవసరం లేదు
import json as _json, re as _re
_MK = _re.compile(r'^(\d+[\.\)]\s|[A-Ea-e][\)\.]\s|\([a-e]\)|\[[a-e]\]|[ivx]+[\)\.]|Q\.|Now,|Ans|\{Q)')
class Src:
    def __init__(self, path): self.P = _json.load(open(path, encoding='utf-8'))
    def __call__(self, p, a, b=None, drop=()):
        L = self.P[str(p)][a - 1:(b or a)]
        L = [x for i, x in enumerate(L, a) if i not in drop]
        out = []
        for x in L:
            s = _re.sub(r'\s{2,}', '  ', x.strip())
            if out and len(prev) >= 68 and not _MK.match(s) and not out[-1].endswith(':'):
                out[-1] += ' ' + s
            else:
                out.append(s)
            prev = x.strip()
        return '\n'.join(out)
    def T(self, *rngs):
        """బహుళ (p,a,b) పరిధులు కలిపి"""
        return '\n'.join(self(*r) for r in rngs)
_STOP = _re.compile(r'^\s*(Q\.\s*No\.?\s*\d|Q\.\s*No\.?\s*:|GRAMMAR|CREATIVE EXPRESSION|READING COMPREHENSION|\(?LEVEL-|SECTION\s*-|JUMBLED|STUDY SKILLS)|^\d+\.\s')
def _until(self, p, a, stop=None, maxp=3):
    """(p,a) నుండి తర్వాతి బ్లాక్ (Q.No / విభాగం) మొదలయ్యే వరకు – పేజీలు దాటి కూడా"""
    st = _re.compile(stop) if isinstance(stop, str) else (stop or _STOP)
    rng, first = [], True
    for pp in range(p, p + maxp):
        L = self.P.get(str(pp), [])
        s = a if pp == p else 1
        e = s
        while e <= len(L):
            if not first and st.match(L[e - 1]): break
            first = False; e += 1
        if e > s: rng.append((pp, s, e - 1))
        if e <= len(L): break
    return self.T(*rng)
Src.until = _until
