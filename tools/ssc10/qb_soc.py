# సాంఘిక శాస్త్రం – Mission March SSC-2027 Action Plan Phase-I ప్రశ్నల బ్యాంక్ (BSE A.P., Social_Final.pdf పేజీలు 6–35)
# ప్రతి అధ్యాయం ఒక ఫైల్: qb_mat/cNN.py → ITEMS = [(tag, lid, marks, q_te, a_te, q_en, a_en, wrong|None, ex_te, ex_en)]
# tag = 'QB<level>-<marks>-<no>'  (level 1 = Rising Star, 2 = Shining Star; no = బ్యాంక్‌లోని ప్రశ్న సంఖ్య)
# ప్రశ్నలు అధికారిక బ్యాంక్‌వి; సాధనలు Claude రాసినవి (NCERT పద్ధతి) – టీచర్ సరిచూసుకోవచ్చు.
import glob, os, importlib.util
ITEMS = []
LESSONS = []   # notes లో లేని పాఠాలు (పౌరశాస్త్రం cv1–cv5)
for f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'qb_soc', 'c*.py'))):
    sp = importlib.util.spec_from_file_location('qb_' + os.path.basename(f)[:-3], f); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    ITEMS += [tuple(x) for x in m.ITEMS]; LESSONS += getattr(m, 'LESSONS', [])
