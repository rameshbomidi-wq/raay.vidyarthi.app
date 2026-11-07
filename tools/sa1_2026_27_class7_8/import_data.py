#!/usr/bin/env python3
"""Import class 7/8 SA1 sources as student-friendly numbered model solutions."""
import argparse
import json
import re
import unicodedata
from pathlib import Path

BATCH = 'sa1-2026-27-class7-8-pointwise'

def norm(t):
    return re.sub(r'\s+',' ',unicodedata.normalize('NFKC',str(t)).lower()).strip()

def load(path,grade):
    if not path.exists(): return {},None,None
    text=path.read_text(encoding='utf-8')
    m=re.search(r'\)\['+str(grade)+r'\]\s*=\s*',text)
    assert m, str(path)
    value,end=json.JSONDecoder().raw_decode(text[m.end():])
    return value,text[:m.end()],text[m.end()+end:]

def save(path,value,prefix,suffix,global_name,grade):
    if prefix is None:
        prefix='/* రాయ్ విద్యార్థి – '+str(grade)+'వ తరగతి SA1 గణితం — పాయింట్‌వైజ్ సాధనలు */\n(window.'+global_name+'=window.'+global_name+'||{})['+str(grade)+']='
        suffix=';\n'
    path.write_text(prefix+json.dumps(value,ensure_ascii=False,separators=(',',':'))+suffix,encoding='utf-8')

def points(rec,language):
    steps=[re.sub(r'^\s*\d+[.)]\s*','',s).strip() for s in rec['steps_'+language]]
    assert len(steps)>=2 and all(steps), rec['qid']
    if norm(rec['answer_'+language]) not in norm(steps[-1]):
        steps.append(('తుది జవాబు: ' if language=='te' else 'Final answer: ')+rec['answer_'+language])
    return steps

def body(rec,language):
    result='\n'.join(f'{i}. {s}' for i,s in enumerate(points(rec,language),1))
    if language=='te' and rec.get('display_note_te'):
        result+='\nగమనిక: '+rec['display_note_te']
    return result

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[2])
    p.add_argument('--sources',type=Path,default=Path(__file__).resolve().parent/'papers')
    p.add_argument('--report',type=Path,default=Path(__file__).resolve().parent/'import_report.json')
    a=p.parse_args();root=a.repo.resolve()
    sources=sorted((json.loads(f.read_text(encoding='utf-8')) for f in a.sources.glob('*.json')),key=lambda d:d['class'])
    assert [d['class'] for d in sources]==[7,8]
    report={'batch':BATCH,'answer_style':'numbered-pointwise','papers':[],'input_records':0,'unique_added':0,'duplicates':[],'issues':[]}
    for src in sources:
        grade=src['class'];records=src['records'];assert src['question_stems_complete'], src['paper_id']+' needs source questions'
        assert [r['qid'] for r in records]==src['expected_qids']
        assert len({r['qid'] for r in records})==len(records)
        book=f"books/{grade}/{src['source_filename']}";assert (root/book).exists()
        notes,np,ns=load(root/f'notes-{grade}.js',grade)
        answers,ap,ass=load(root/f'answers-{grade}.js',grade)
        notes.setdefault('mat',[])
        notes['mat']=[L for L in notes['mat'] if L.get('source_batch')!=BATCH]
        seen={norm(q[0]):'existing-note:'+L['id'] for L in notes['mat'] for q in L.get('qa',[])+L.get('qz',[])+L.get('wb',{}).get('qz',[])}
        qa=[];quiz=[];rich=[];teacher=[];page_answers={str(pg):[f'— {grade}వ తరగతి SA1 గణితం మోడల్ పేపర్ 1 —', 'అందించిన సాధనలను పరిశీలించి పాయింట్‌వైజ్‌గా సిద్ధం చేసిన నమూనా జవాబులు; అధికారిక కీ అని పేర్కొనలేదు.'] for pg in range(1,src['pages']+1)}
        added=0
        for r in records:
            assert all(r[k].strip() for k in ('question_en','question_te','answer_en','answer_te'))
            assert 1<=r['page']<=src['pages']
            assert r['marks'] is None or isinstance(r['marks'],int) and r['marks']>0
            q=f"ప్ర. {r['qid']}"+(f" ({r['marks']} మార్కులు)" if r['marks'] is not None else '')+' — '+r['question_te']
            text=body(r,'te');english=body(r,'en')
            steps=points(r,'te')
            pages={r['page']}
            if r.get('answer_page'):
                assert 1<=r['answer_page']<=src['pages'];pages.add(r['answer_page'])
            oe,ot,ci=r['options_en'],r['options_te'],r['correct_index']
            usable=ci is not None and len(oe)==len(ot)==4
            if ci is not None:
                assert usable and 0<=ci<4 and r['answer_en']==oe[ci] and r['answer_te']==ot[ci],r['qid']
            for pg in pages:
                page_answers[str(pg)]+=['— ప్ర. '+r['qid']+' —',r['question_te']]
                if ot:page_answers[str(pg)]+=['  '.join(f"{'ABCD'[i]}) {x}" for i,x in enumerate(ot))]
                # Each step is a separate ordered-list entry in the existing PDF answer panel.
                page_answers[str(pg)]+=[f'దశ {i}: {s}' for i,s in enumerate(steps,1)]
                if r.get('display_note_te'):page_answers[str(pg)]+=['గమనిక: '+r['display_note_te']]
            teacher+=[q,*[f'{i}. {s}' for i,s in enumerate(steps,1)]]
            if r.get('issue_notes'):report['issues'].append({'record':src['paper_id']+':'+r['qid'],'notes':r['issue_notes']})
            keys=[norm(r['question_'+lang]+' | '+' | '.join(r['options_'+lang])) for lang in ('te','en')]
            reference=next((seen[key] for key in keys if key in seen),None)
            if reference:
                report['duplicates'].append({'record':src['paper_id']+':'+r['qid'],'reference':reference});continue
            added+=1
            for key in keys:seen[key]=src['paper_id']+':'+r['qid']
            display=q
            if ot:display+='\n'+'  '.join(f"{'ABCD'[i]}) {x}" for i,x in enumerate(ot))
            qa.append([display,text])
            # Existing rich-text data block honours newlines without modifying app CSS.
            rich.append([f'ప్ర. {r["qid"]} — పాయింట్‌వైజ్ సాధన',r['question_te']+'\n\n'+text])
            if usable:
                assert len(set(ot))==4
                quiz.append([q,r['answer_te'],*[x for i,x in enumerate(ot) if i!=ci]])
        lesson={'id':'sa1mp1','no':101,'t':'SA1 గణితం మోడల్ పేపర్ 1 — పాయింట్‌వైజ్ సాధనలు (2026–27)','m':[10,11],'ty':'SA1 మోడల్ పేపర్','th':'సులభమైన దశలవారీ సాధనలు','by':src['source_filename'],'sum':f'{grade}వ తరగతి గణితం SA1 మోడల్ పేపర్. ఇచ్చిన వివరాలు, సూత్రం, దశలవారీ లెక్క, యూనిట్లతో చివరి జవాబును పాయింట్‌వైజ్‌గా ఇచ్చాం. పాయింట్‌వైజ్ సాధనల భాగంలో ప్రతి దశ కొత్త లైన్‌లో కనిపిస్తుంది. మూల PDFలో ప్రశ్నలతో పాటు ఇచ్చిన సాధనలు కూడా ఉన్నాయి.','pts':['మొదట ప్రశ్న చదివి ఇచ్చిన వివరాలు గుర్తించండి.','సరైన సూత్రం రాసి విలువలు ప్రతిక్షేపించండి.','ప్రతి మధ్య దశను క్రమంగా రాయండి.','చివరి జవాబు వద్ద అవసరమైన యూనిట్లు రాయండి.','నిరూపణలో ప్రతి ముఖ్య దశకు కారణం ఇవ్వండి.'],'w':[],'gr':{'t':'పరీక్షలో జవాబు రాసే క్రమం','p':['ఇచ్చినవి → సూత్రం → సాధన దశలు → తుది జవాబు']},'qa':qa,'fg':rich,'act':'పాయింట్‌వైజ్ సాధనలను చదివి, పేపర్‌లోని ప్రశ్నలకు సొంతంగా జవాబులు రాయండి.','kn':'మూల PDFలో ముద్రించిన జవాబులను answer-lock దాచదు. Existing lock అదనంగా చేర్చిన answer panelకే వర్తిస్తుంది. QAలోని దశల line breaks కోసం పైన ఉన్న పాయింట్‌వైజ్ సాధనల భాగం చూడండి.','qz':quiz,'wb':{'pg':f'1–{src["pages"]}','p':1,'f':book,'lb':'SA1 ప్రశ్నలు – సాధనలు','ws':['విభాగం I','విభాగం II','విభాగం III','విభాగం IV'],'mis':'సాధనలో ముఖ్యమైన మధ్య దశలు వదలవద్దు; చివరి జవాబుకు యూనిట్లు జతచేయండి.','qz':[]},'tg':[['పాయింట్‌వైజ్ నమూనా సాధనలు',teacher]],'source_batch':BATCH,'source_paper':src['paper_id'],'answer_style':'numbered-pointwise'}
        notes['mat'].append(lesson);answers[src['source_filename']]=page_answers
        save(root/f'notes-{grade}.js',notes,np,ns,'RAAY_TB',grade);save(root/f'answers-{grade}.js',answers,ap,ass,'RAAY_ANS',grade)
        report['input_records']+=len(records);report['unique_added']+=added
        report['papers'].append({'paper_id':src['paper_id'],'class':grade,'records':len(records),'unique_added':added,'quiz_items':len(quiz),'qa_items':len(qa),'pages':src['pages'],'source_has_solutions':src['source_has_solutions'],'source_options_only':True})
    a.report.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
