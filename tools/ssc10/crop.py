"""PDF పేజీ నుండి బొమ్మ కత్తిరించి ssc/img/ లో jpg గా పెట్టడం.
python3 tools/ssc10/crop.py <pdf> <page> <x0> <y0> <x1> <y1> <out-name> [prevdpi=80]
x/y = prevdpi (డిఫాల్ట్ 80) వద్ద రెండర్ చేసిన పేజీ బొమ్మలోని పిక్సెల్ నిరూపకాలు. ఫలితం: ssc/img/<out-name>.jpg (వెడల్పు ≤ 520)"""
import sys, subprocess, tempfile, os
from PIL import Image
pdf, page, x0, y0, x1, y1, name = sys.argv[1], int(sys.argv[2]), *map(float, sys.argv[3:7]), sys.argv[7]
prev = float(sys.argv[8]) if len(sys.argv) > 8 else 80; D = 200
REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with tempfile.TemporaryDirectory() as td:
    subprocess.run(['pdftoppm', '-r', str(D), '-png', '-f', str(page), '-l', str(page), pdf, td + '/p'], check=True)
    f = [x for x in os.listdir(td) if x.endswith('.png')][0]; im = Image.open(td + '/' + f).convert('RGB')
k = D / prev; im = im.crop((int(x0 * k), int(y0 * k), int(x1 * k), int(y1 * k)))
if im.width > 520: im = im.resize((520, int(im.height * 520 / im.width)), Image.LANCZOS)
out = os.path.join(REPO, 'ssc/img', name + '.jpg'); os.makedirs(os.path.dirname(out), exist_ok=True)
im.save(out, quality=72, optimize=True); print(out, im.size, os.path.getsize(out))
