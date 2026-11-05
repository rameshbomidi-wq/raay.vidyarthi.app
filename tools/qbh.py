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
