#!/usr/bin/env python3
"""Import SA1 model-paper content; never edit application code or merge branches."""
from __future__ import annotations
import argparse
import json
import re
import unicodedata
from pathlib import Path

PREFIX_RE = re.compile(r'^SA1[^\n]*\n', re.I)

def norm(text):
    text = PREFIX_RE.sub('', str(text))
    text = re.sub(r'\n?⟦(?:fig|img):[\s\S]*?⟧', '', text)
    text = unicodedata.normalize('NFKC', text).lower()
    text = text.replace('−', '-').replace('–', '-').replace('×', '*').replace('÷', '/')
    text = re.sub(r'[“”‘’"?.,:;!_]', '', text)
    return re.sub(r'\s+', ' ', text).strip()

def read_js(path, grade):
    text = path.read_text(encoding='utf-8')
    match = re.search(r'\)\[' + str(grade) + r'\]\s*=\s*', text)
    if not match:
        raise ValueError(f'Unsupported data assignment: {path}')
    value, length = json.JSONDecoder().raw_decode(text[match.end():])
    return value, text[:match.end()], text[match.end()+length:]

def write_js(path, value, prefix, suffix):
    encoded = json.dumps(value, ensure_ascii=False, separators=(',', ':'))
    path.write_text(prefix + encoded + suffix, encoding='utf-8')

def new_js(path, global_name, grade, value, label):
    write_js(path, value, '/* '+label+' */\n(window.'+global_name+'=window.'+global_name+'||{})['+str(grade)+']=', ';\n')

def question_prefix(paper, rec, language='te'):
    if language == 'en':
        return f"SA1 2026–27 | Model {paper['model']} | Q.{rec['qid']} | {rec['marks']} marks\n"
    return f"SA1 2026–27 • మోడల్ {paper['model']} • ప్ర. {rec['qid']} • {rec['marks']} మార్కులు\n"

def full_solution(rec, language):
    answer, solution = rec['answer_'+language], rec['solution_'+language]
    body = solution or answer
    if answer and answer not in body:
        body += '\n' + ('జవాబు: ' if language == 'te' else 'Answer: ') + answer
    if rec.get('_display_note'):
        body += ('\nగమనిక: ' + rec['_display_note']) if language == 'te' else ('\nNote: ' + ' '.join(rec.get('issue_notes', [])))
    return body

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument('--papers', type=Path, default=Path(__file__).resolve().parent/'papers')
    parser.add_argument('--review', type=Path, default=Path(__file__).resolve().parent/'duplicate_review.json')
    parser.add_argument('--report', type=Path, default=Path(__file__).resolve().parent/'import_report.json')
    args = parser.parse_args()
    root = args.repo.resolve()
    papers = sorted((json.loads(p.read_text(encoding='utf-8')) for p in args.papers.glob('*.json')), key=lambda p:(p['class'],p['model']))
    assert [(p['class'],p['model']) for p in papers] == [(9,1),(9,2),(9,3),(10,1),(10,2),(10,3)], 'All six papers are required'
    overrides = json.loads(args.review.read_text(encoding='utf-8')) if args.review.exists() else {}
    notes_path = args.review.parent/'display_notes.json'
    display_notes = json.loads(notes_path.read_text(encoding='utf-8')) if notes_path.exists() else {}
    note10, nprefix, nsuffix = read_js(root/'notes-10.js', 10)
    ans10, aprefix, asuffix = read_js(root/'answers-10.js', 10)
    ssc10, sprefix, ssuffix = read_js(root/'ssc-10.js', 10)
    # Preserve all pre-existing lessons/subjects and all non-SA1 bank items.
    note10['mat'] = [x for x in note10['mat'] if x.get('source_batch') != 'sa1-2026-27']
    ssc10['mat'] = [x for x in ssc10['mat'] if not (len(x)>7 and str(x[7]).startswith('SA1-2627-')) and not str(x[2]).startswith('SA1 2026')]
    note9 = read_js(root/'notes-9.js',9)[0] if (root/'notes-9.js').exists() else {'mat': []}
    note9['mat'] = [x for x in note9.get('mat',[]) if x.get('source_batch') != 'sa1-2026-27']
    ans9 = read_js(root/'answers-9.js',9)[0] if (root/'answers-9.js').exists() else {}
    existing = {9:{},10:{}}
    for i, rec in enumerate(ssc10['mat']):
        for text in (rec[2], rec[5] if len(rec)>5 else ''):
            if text:
                existing[10].setdefault(norm(text), 'existing-ssc:'+str(i))
    for lesson in note10['mat']:
        for q in lesson.get('qa',[]):
            existing[10].setdefault(norm(q[0]), 'existing-note:'+lesson['id'])
        for q in lesson.get('qz',[]) + lesson.get('wb',{}).get('qz',[]):
            existing[10].setdefault(norm(q[0]), 'existing-note:'+lesson['id'])
    for lesson in note9['mat']:
        for q in lesson.get('qa',[]) + lesson.get('qz',[]) + lesson.get('wb',{}).get('qz',[]):
            existing[9].setdefault(norm(q[0]), 'existing-note:'+lesson['id'])
    report = {'batch':'sa1-2026-27','papers':[],'input_records':0,'unique_added':{'9':0,'10':0},'duplicates':[],'issues':[]}
    valid10 = {x['id'] for x in note10['mat']}
    for paper in papers:
        grade, model, pid = paper['class'], paper['model'], paper['paper_id']
        path = root/'books'/str(grade)/paper['source_filename']
        assert path.exists(), 'Missing source PDF: '+str(path)
        records = paper['records']
        assert len({x['qid'] for x in records}) == len(records), pid
        assert all(1<=x['page']<=paper['pages'] for x in records), pid
        report['input_records'] += len(records)
        bodyqa, quizzes, teacher = [], [], []
        answers = {str(i):[f"— {grade}వ తరగతి గణితం SA1 2026–27 మోడల్ పేపర్ {model} —", 'AI రూపొందించిన నమూనా సాధనలు; అధికారిక జవాబు కీ కాదు.'] for i in range(1,paper['pages']+1)}
        added = skipped = 0
        for rec in records:
            assert rec['marks'] in (1,2,4,8), (pid,rec['qid'],rec['marks'])
            assert all(isinstance(rec[k], str) and rec[k].strip() for k in ('question_en','question_te','answer_en','answer_te','solution_en','solution_te')), (pid,rec['qid'])
            oe, ot, ci = rec['options_en'], rec['options_te'], rec['correct_index']
            usable_mcq = ci is not None and len(oe)==len(ot)==4 and len(set(ot))==4 and 0<=ci<4
            if ci is not None:
                assert 0<=ci<len(oe) and len(oe)==len(ot), (pid,rec['qid'])
                assert rec['answer_en']==oe[ci] and rec['answer_te']==ot[ci], (pid,rec['qid'],'answer must be exact option')
            if grade==10:
                assert rec['lesson_id'] in valid10, (pid,rec['qid'],rec['lesson_id'])
            aid = pid+':'+rec['qid']
            rec['_display_note'] = display_notes.get(aid, '')
            ref = next((existing[grade][norm(t)] for t in (rec['question_en'],rec['question_te']) if norm(t) in existing[grade]), None)
            if aid in overrides and overrides[aid].get('duplicate'):
                ref = overrides[aid]['reference']
            sol = full_solution(rec, 'te')
            qte = question_prefix(paper,rec) + rec['question_te']
            qen = question_prefix(paper,rec,'en') + rec['question_en']
            page_lines = answers[str(rec['page'])]
            page_lines += [qte]
            if ot:
                page_lines += ['  '.join(f"{'ABCD'[i]}) {v}" for i,v in enumerate(ot))]
            page_lines += ['జవాబు: '+rec['answer_te'], 'సాధన: '+sol, 'English question: '+rec['question_en'], 'Model solution: '+full_solution(rec,'en')]
            teacher.append(f"ప్ర. {rec['qid']} ({rec['marks']} మా.)\n{rec['question_te']}\n{sol}")
            if rec.get('issue_notes'):
                report['issues'].append({'record':aid,'notes':rec['issue_notes']})
            if ref:
                report['duplicates'].append({'record':aid,'reference':ref,'question_en':rec['question_en']})
                skipped += 1
                continue
            for text in (rec['question_en'], rec['question_te']):
                existing[grade][norm(text)] = aid
            added += 1
            report['unique_added'][str(grade)] += 1
            if usable_mcq:
                wrong = [v for i,v in enumerate(ot) if i!=ci]
                quizzes.append([qte, rec['answer_te'], *wrong])
            else:
                question = qte
                if ot:
                    question += '\n'+'  '.join(f"{'ABCD'[i]}) {v}" for i,v in enumerate(ot))
                if rec.get('question_figure'):
                    question += '\nచిత్రం కోసం క్రింద ఉన్న మూల పేపర్‌లో ప్ర. '+rec['qid']+' చూడండి.'
                bodyqa.append([question,sol])
            if grade==10:
                tag = f"SA1-2627-P{model}-Q{rec['qid']}"
                w = [v for i,v in enumerate(ot) if i!=ci] if usable_mcq else 0
                at = rec['answer_te'] if usable_mcq else sol
                ae = rec['answer_en'] if usable_mcq else full_solution(rec,'en')
                bank_qte, bank_qen = qte, qen
                if rec.get('question_figure'):
                    figure = rec['question_figure']
                    assert (root/figure).exists(), figure
                    marker = '\n⟦img:'+figure+'|మూల SA1 పేపర్‌లోని గ్రాఫ్⟧'
                    bank_qte += marker
                    bank_qen += marker
                row = [rec['lesson_id'],rec['marks'],bank_qte,at,w,bank_qen,ae,tag,sol if usable_mcq else '',full_solution(rec,'en') if usable_mcq else '']
                if usable_mcq:
                    row.append(ci)
                ssc10['mat'].append(row)
        lesson = {'id':f'sa1mp{model}','no':100+model,'t':f'SA1 గణితం మోడల్ పేపర్ {model} (2026–27)','m':[10,11],'ty':'SA1 మోడల్ పేపర్','th':'ప్రశ్నలు – నమూనా సాధనలు','by':paper['source_filename'],'sum':f'{grade}వ తరగతి గణితం SA1 మోడల్ పేపర్ {model}. పేపర్‌లోని అన్ని ప్రశ్నలు, అంతర్గత ఎంపికలు PDFలో ఉన్నాయి. కొత్త ప్రత్యేక ప్రశ్నలు నోట్స్/టెస్ట్‌లో చేర్చబడ్డాయి; నకలు ప్రశ్నలు బ్యాంక్‌లో మళ్ళీ చేర్చలేదు. PDF పేజీ వారీ జవాబులు మరియు పూర్తి సాధనలు అందుబాటులో ఉన్నాయి. ఇవి AI రూపొందించిన నమూనా సాధనలు; అధికారిక జవాబు కీ కాదు.','pts':[f'మూల పేపర్: {paper["pages"]} PDF పేజీలు.',f'అన్ని ఎంపికలతో {len(records)} ప్రశ్న అంశాలకు సాధనలు.',f'ఈ పేపర్ నుంచి కొత్తగా {added} ప్రశ్నలు; నకలు {skipped}.','ప్రశ్నలలో ఇచ్చిన సంఖ్యలు, యూనిట్లు, మార్కులు మూల పేపర్ ప్రకారం ఉంచబడ్డాయి.'],'w':[],'gr':{'t':'రివిజన్','p':[]},'qa':bodyqa,'act':'మొదట మూల పేపర్‌లోని ప్రశ్నలకు సొంతంగా జవాబులు రాయండి. తర్వాత నమూనా సాధనలతో పోల్చుకోండి.','kn':'మూల పేపర్‌లో దోషం/అస్పష్టత ఉంటే సాధనలో గమనిక ఇవ్వబడింది. గణిత చిత్రాలకు ప్రశ్నలో ఇచ్చిన labels/విలువలు అనుసరించండి.','qz':quizzes,'wb':{'pg':f'1–{paper["pages"]}','f':f'books/{grade}/{paper["source_filename"]}','p':1,'ws':['విభాగం I','విభాగం II','విభాగం III','విభాగం IV'],'mis':'OR ఉన్న ప్రశ్నలలో పరీక్షలో సూచించిన ఎంపిక మాత్రమే రాయాలి; రివిజన్ కోసం రెండు సాధనలూ ఇచ్చాం.','qz':[],'lb':'SA1 మోడల్ పేపర్'},'tg':[[f'SA1 మోడల్ పేపర్ {model} — అన్ని ప్రశ్నల సాధనలు',teacher]],'source_batch':'sa1-2026-27','source_paper':pid}
        if grade==9:
            note9['mat'].append(lesson)
            ans9[paper['source_filename']] = answers
        else:
            note10['mat'].append(lesson)
            ans10[paper['source_filename']] = answers
        report['papers'].append({'paper_id':pid,'records':len(records),'unique_added':added,'duplicates_skipped':skipped,'quiz_items':len(quizzes),'qa_items':len(bodyqa),'pages':paper['pages'],'answer_key_present':paper['answer_key_present']})
    new_js(root/'notes-9.js','RAAY_TB',9,note9,'రాయ్ విద్యార్థి – 9వ తరగతి SA1 గణితం మోడల్ పేపర్లు 2026–27')
    new_js(root/'answers-9.js','RAAY_ANS',9,ans9,'రాయ్ విద్యార్థి – 9వ తరగతి SA1 గణితం PDF పేజీ వారీ నమూనా సాధనలు')
    write_js(root/'notes-10.js',note10,nprefix,nsuffix)
    write_js(root/'answers-10.js',ans10,aprefix,asuffix)
    write_js(root/'ssc-10.js',ssc10,sprefix,ssuffix)
    args.report.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__ == '__main__':
    main()
