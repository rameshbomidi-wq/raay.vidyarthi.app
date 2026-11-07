/* Read-only data/runtime validation. Run: node tools/sa1_2026_27/validate.cjs [baseline.json] */
const fs = require('fs');
const path = require('path');
const vm = require('vm');
const assert = require('assert/strict');
const crypto = require('crypto');
const root = path.resolve(__dirname,'../..');
const window = {};
const context = {window, console, V:{}, S:{cur:{c:9},bookPos:{}}, T:{}, TBE:{c:9}, param:{s:'mat',id:'sa1mp1'}, view:'tbl',
  SUBJ:{mat:{n:'గణితం',col:'#2563eb',bg:'#eff6ff',ic:''}},
  TB_MN:Array.from({length:12},(_,i)=>String(i+1)),TB_AB:Array.from({length:12},(_,i)=>String(i+1)),
  live:()=>[], learnSubs:()=>['mat'], myRes:()=>[], isRead:()=>false, readMap:()=>({}),
  esc:t=>String(t??'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'),
  shuffle:a=>a.slice(),go:()=>{},toast:()=>{},save:()=>{},tick:null,
  setInterval:()=>1,setTimeout:()=>1,softRender:()=>{},mmss:()=>'',
  pdfInit:()=>{},
  document:{head:{appendChild:()=>{}},createElement:()=>({remove:()=>{}})},me:()=> 'test'};
vm.createContext(context);
for (const name of ['notes-9.js','answers-9.js','notes-10.js','answers-10.js','ssc-10.js']) {
  vm.runInContext(fs.readFileSync(path.join(root,name),'utf8'),context,{timeout:3000,filename:name});
}
const index = fs.readFileSync(path.join(root,'index.html'),'utf8');
const section=(from,to)=>index.slice(index.indexOf(from),index.indexOf(to));
vm.runInContext(section('const TB_SK=','/* ---------- 🎓 SSC'),context,{timeout:3000});
vm.runInContext(section('window.RAAY_SSC=','/* 🖼 బొమ్మలు/పట్టికలు'),context,{timeout:3000});
vm.runInContext(section('window.RAAY_ANS=','function ansLessonOf'),context,{timeout:3000});
const plain = x=>JSON.parse(JSON.stringify(x));
const report=JSON.parse(fs.readFileSync(path.join(__dirname,'import_report.json'),'utf8'));
assert.equal(report.input_records,228);
assert.equal(report.duplicates.length,6);
assert.equal(report.unique_added['9'],114);
assert.equal(report.unique_added['10'],108);
let quizCount=0,qaCount=0,pageKeys=0;
for (const grade of [9,10]) {
  const lessons=window.RAAY_TB[grade].mat.filter(x=>x.source_batch==='sa1-2026-27');
  assert.equal(lessons.length,3);
  assert.equal(new Set(window.RAAY_TB[grade].mat.map(x=>x.id)).size,window.RAAY_TB[grade].mat.length);
  for (const L of lessons) {
    assert.equal(L.wb.p,1);
    assert.ok(fs.existsSync(path.join(root,L.wb.f)));
    const paper=JSON.parse(fs.readFileSync(path.join(__dirname,'papers',L.source_paper+'.json'),'utf8'));
    const expected=[...Array(28)].map((_,i)=>String(i+1)).concat(...[29,30,31,32,33].map(n=>[n+'a',n+'b']));
    assert.deepEqual(paper.records.map(r=>r.qid),expected);
    assert.equal(paper.records.length,38);
    const A=window.RAAY_ANS[grade][path.basename(L.wb.f)];
    assert.equal(Object.keys(A).length,paper.pages);
    pageKeys+=Object.keys(A).length;
    for (const r of paper.records) {
      assert.ok(A[r.page].some(x=>x.startsWith(`SA1 2026–27 • మోడల్ ${paper.model} • ప్ర. ${r.qid} •`)),`${paper.paper_id} Q${r.qid}: missing page answer`);
      assert.ok(r.answer_en && r.answer_te && r.solution_en && r.solution_te);
      if (r.question_figure) assert.ok(fs.existsSync(path.join(root,r.question_figure)));
    }
    for (const q of L.qz) {
      assert.equal(q.length,5);
      assert.equal(new Set(q.slice(1)).size,4);
    }
    quizCount+=L.qz.length;qaCount+=L.qa.length;
    context.S.cur.c=grade;context.param={s:'mat',id:L.id};context.view='tbl';
    const html=vm.runInContext('V.tbl()',context);
    assert.ok(html.includes(L.t));
    assert.ok(html.includes(`tbWbOpen('mat','${L.id}')`));
    vm.runInContext(`tbWbOpen('mat','${L.id}')`,context);
    assert.equal(context.S.bookPos[L.wb.f],1);
    assert.ok(!html.includes('undefined'));
    vm.runInContext(`startLesTest('mat','${L.id}',0)`,context);
    assert.equal(context.T.qs.length,Math.min(10,L.qz.length));
    for (const q of context.T.qs) assert.ok(q.o.includes(q.a));
    context.view='book';context.param={};
    for (const pg of Object.keys(A)) {
      assert.deepEqual(plain(vm.runInContext(`ansPage('${L.wb.f}',${pg})`,context)),plain(A[pg]));
    }
  }
}
const rows=window.RAAY_SSC[10].mat.filter(x=>x[7]?.startsWith('SA1-2627-'));
assert.equal(rows.length,108);
assert.equal(new Set(rows.map(x=>x[7])).size,108);
assert.equal(rows.filter(x=>x[2].includes('⟦img:')).length,3);
for (const x of rows) {
  assert.ok([1,2,4,8].includes(x[1]));
  assert.ok(window.RAAY_TB[10].mat.some(L=>L.id===x[0]));
  assert.ok(x[2]&&x[3]&&x[5]&&x[6]);
  if(x[4]) {
    assert.equal(x[4].length,3);
    assert.equal(new Set(x[4]).size,3);
    assert.ok(!x[4].includes(x[3]));
    assert.ok(Number.isInteger(x[10])&&x[10]>=0&&x[10]<4);
  }
}
const items=vm.runInContext("sscItems('mat')",context);
assert.equal(new Set(items.map(x=>x.id)).size,items.length);
for (const x of items.filter(x=>x.bd.startsWith('SA1-2627-'))) {
  if(x.o) assert.ok(x.o.includes(x.a));
}
if(process.argv[2]) {
  const base=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
  assert.deepEqual(plain(window.RAAY_TB[10].mat.filter(x=>x.source_batch!=='sa1-2026-27')),base.RAAY_TB['10'].mat);
  for(const s of Object.keys(base.RAAY_TB['10']).filter(s=>s!=='mat')) assert.deepEqual(plain(window.RAAY_TB[10][s]),base.RAAY_TB['10'][s]);
  for(const [book,data] of Object.entries(base.RAAY_ANS['10'])) assert.deepEqual(plain(window.RAAY_ANS[10][book]),data);
  assert.deepEqual(plain(window.RAAY_SSC[10].mat.filter(x=>!x[7]?.startsWith('SA1-2627-'))),base.RAAY_SSC['10'].mat);
  for(const s of Object.keys(base.RAAY_SSC['10']).filter(s=>s!=='mat')) assert.deepEqual(plain(window.RAAY_SSC[10][s]),base.RAAY_SSC['10'][s]);
  for(const global of ['RAAY_SSC_BM','RAAY_SSC_LN','RAAY_MM']) assert.deepEqual(plain(window[global]),base[global]);
}
console.log(JSON.stringify({status:'PASS',source_records:228,new_unique_questions:222,duplicates_skipped:6,new_revision_lessons:6,quiz_questions:quizCount,qa_questions:qaCount,new_ssc_questions:rows.length,answer_pdf_pages:pageKeys,source_graphs:3,checks:['source coverage','existing data preservation','data schema','quiz answer membership','notes render fixtures','PDF answer lookup','SSC IDs and source images']},null,2));
