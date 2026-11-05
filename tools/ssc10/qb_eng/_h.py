# English బ్యాంక్ ఫైళ్ళకు సాధారణ సహాయకాలు
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from qbh import Bank, Src
S = Src(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src_pages.json'))
RCH = '(Q.No. 1–5 · 5 × 1 = 5 marks) '
class EB(Bank):
    def rc(self, L, p, a, ans, lid=None, stop=None):
        """పఠన అవగాహన – పేరా + 5 ప్రశ్నలు ఒకే అంశం (4 మార్కుల విభాగంలో)"""
        return self.q(L, 4, S.until(p, a, stop), ans, lid=lid)
    def g(self, L, instr, items, mk=1, lid=None):
        """వ్యాకరణం: instr = (p,a[,b]); items = [((p,a[,b]), జవాబు[, lid]), ...] – ప్రతి ఉప ప్రశ్న వేరు అంశం"""
        I = S(*instr)
        for it in items:
            r, ans = it[0], it[1]
            self.q(L, mk, I + '\n' + S(*r), ans, lid=(it[2] if len(it) > 2 else lid))
        return self
    def ce(self, L, rng, ans, lid=None, mk=8):
        return self.q(L, mk, S.T(*rng) if isinstance(rng[0], tuple) else S(*rng), ans, lid=lid)
def _rcr(self, L, rngs, ans, lid=None, mk=4):
    """స్పష్టమైన (p,a,b) పరిధులతో పఠన బ్లాక్"""
    return self.q(L, mk, S.T(*rngs), ans, lid=lid)
EB.rcr = _rcr
IMG = lambda path, cap='': f'\n⟦img:ssc/img/{path}.jpg|{cap}⟧'
