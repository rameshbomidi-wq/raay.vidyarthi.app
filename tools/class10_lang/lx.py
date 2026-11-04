import sys,re
a,b,start=int(sys.argv[1]),int(sys.argv[2]),sys.argv[3] if len(sys.argv)>3 else None
on=start is None
for p in range(a,b+1):
    out=[]
    for l in open(f'ocr_tel/{p}.txt').read().splitlines():
        L=l.strip()
        if not on and start and start in L: on=True
        if not on: continue
        if len(L)<4 or 'తెలుగు వాచకం' in L or 'తెలుగు పరిమళం' in L: continue
        if re.fullmatch(r'[\W\dA-Za-z ]+',L) and len(L)<12: continue
        out.append(L[:160])
    if out: print(f'##{p}'); print('\n'.join(out))
