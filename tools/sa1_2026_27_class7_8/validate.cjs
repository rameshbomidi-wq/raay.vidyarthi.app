/* Class 7/8 data and existing-renderer fixtures; no app/server state is changed. */
const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert/strict');
const root=path.resolve(__dirname,'../..');
const el={innerHTML:'',hidden:true};
const c={window:{},V:{},S:{cur:{c:7},bookPos:{}},T:{},TBE:{c:7},param:{s:'mat',id:'sa1mp1'},view:'tbl',
  SUBJ:{mat:{n:'గణితం',ic:'',col:'#2563eb',bg:'#eff6ff'}},TB_MN:Array.from({length:12},(_,i)=>String(i+1)),TB_AB:Array.from({length:12},(_,i)=>String(i+1)),
  live:()=>[],myRes:()=>[],isRead:()=>false,readMap:()=>({}),learnSubs:()=>['mat'],
  esc:t=>String(t??'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'),
  shuffle:a=>a.slice(),toast:()=>{},go:()=>{},save:()=>{},pdfInit:()=>{},setInterval:()=>1,setTimeout:()=>1,tick:null,softRender:()=>{},mmss:()=>'',
  BV:{url:'',page:1},INK:{showAns:true},akState:()=>({open:true}),
  document:{head:{appendChild:()=>{}},createElement:()=>({remove:()=>{}}),getElementById:()=>el}};
vm.createContext(c);
for(const name of ['notes-7.js','answers-7.js','notes-8.js','answers-8.js'])vm.runInContext(fs.readFileSync(path.join(root,name),'utf8'),c,{timeout:3000,filename:name});
const text=fs.readFileSync(path.join(root,'index.html'),'utf8');
const fragment=(a,b)=>text.slice(text.indexOf(a),text.indexOf(b));
vm.runInContext(fragment('const TB_SK=','/* ---------- 🎓 SSC'),c,{timeout:3000});
vm.runInContext(fragment('function richT(t)','function figSVG(o)'),c,{timeout:3000});
vm.runInContext(fragment('window.RAAY_ANS=','function ansLessonOf'),c,{timeout:3000});
vm.runInContext(fragment('function ansPanel()','/* విద్యార్థి: జవాబుల పొర'),c,{timeout:3000});
let sourceCount=0,pointCount=0,quizCount=0,pages=0;
for(const grade of [7,8]){
  const data=JSON.parse(fs.readFileSync(path.join(__dirname,'papers',`class${grade}-sa1-model1.json`),'utf8'));
  assert.equal(data.records.length,37);assert.equal(data.question_stems_complete,true);assert.equal(data.source_has_solutions,true);
  assert.deepEqual(data.records.map(x=>x.qid),data.expected_qids);
  assert.deepEqual([...new Set(data.records.map(x=>parseInt(x.qid)))],Array.from({length:33},(_,i)=>i+1));
  const L=c.window.RAAY_TB[grade].mat.find(x=>x.source_batch==='sa1-2026-27-class7-8-pointwise');
  assert.ok(L);assert.equal(L.qa.length,37);assert.equal(L.fg.length,37);assert.equal(L.qz.length,20);assert.equal(L.answer_style,'numbered-pointwise');
  assert.ok(fs.existsSync(path.join(root,L.wb.f)));
  const A=c.window.RAAY_ANS[grade][path.basename(L.wb.f)];assert.equal(Object.keys(A).length,8);pages+=8;
  for(const r of data.records){
    assert.ok(r.question_te&&r.question_en&&r.answer_te&&r.answer_en);
    for(const lang of ['te','en']){
      assert.ok(r['steps_'+lang].length>=2);assert.ok(r['steps_'+lang].every(s=>s.trim()));
    }
    const q=L.qa.find(x=>x[0].startsWith('ప్ర. '+r.qid+' '));assert.ok(q,r.qid);
    assert.ok(q[1].startsWith('1. '));assert.ok(q[1].includes('\n2. '));
    assert.ok(A[r.page].includes('— ప్ర. '+r.qid+' —'));assert.ok(A[r.page].some(x=>x.startsWith('దశ 1:')));
    if(r.correct_index!==null){
      assert.equal(r.options_te.length,4);assert.equal(r.options_en.length,4);
      assert.equal(r.answer_te,r.options_te[r.correct_index]);assert.equal(r.answer_en,r.options_en[r.correct_index]);
      assert.equal(new Set(r.options_te).size,4);
    }
    pointCount+=r.steps_te.length;
  }
  for(const q of L.qz){assert.equal(q.length,5);assert.equal(new Set(q.slice(1)).size,4);}
  c.S.cur.c=grade;c.param={s:'mat',id:L.id};c.view='tbl';
  const html=vm.runInContext('V.tbl()',c);
  assert.ok(html.includes('పాయింట్‌వైజ్'));assert.ok(html.includes('<br>2. '),'rich-text steps must render as distinct lines');assert.ok(!html.includes('undefined'));
  vm.runInContext("tbWbOpen('mat','sa1mp1')",c);assert.equal(c.S.bookPos[L.wb.f],1);
  vm.runInContext("startLesTest('mat','sa1mp1',0)",c);assert.equal(c.T.qs.length,10);assert.ok(c.T.qs.every(q=>q.o.includes(q.a)));
  c.view='book';c.param={};c.BV.url=L.wb.f;
  for(const pg of Object.keys(A)){
    c.BV.page=+pg;vm.runInContext('ansPanel()',c);assert.ok(el.innerHTML.includes('<ol class="ansl">'));
    if(A[pg].some(x=>x.startsWith('దశ 1:')))assert.ok(el.innerHTML.includes('<li>దశ 1:'));
  }
  sourceCount+=37;quizCount+=20;
}
assert.equal(sourceCount,74);assert.equal(quizCount,40);
const report=JSON.parse(fs.readFileSync(path.join(__dirname,'import_report.json'),'utf8'));
assert.equal(report.unique_added,74);assert.equal(report.duplicates.length,0);
console.log(JSON.stringify({status:'PASS',source_questions:sourceCount,source_mcqs:quizCount,telugu_solution_points:pointCount,pdf_pages_indexed:pages,checks:['question/OR coverage','source solution provenance','point-wise arrays','MCQ option membership','actual rich-text line-break rendering','PDF answer panel separate points','paper-open and quiz fixtures']},null,2));
