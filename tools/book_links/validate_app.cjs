/* Existing library runtime fixtures. Does not contact school servers or CSE. */
const fs=require('fs'),path=require('path'),vm=require('vm'),assert=require('assert/strict'),cp=require('child_process');
const root=path.resolve(__dirname,'../..'),html=fs.readFileSync(path.join(root,'index.html'),'utf8');
const start=html.indexOf('const TOK='),end=html.indexOf('V.book=()=>');
assert.ok(start>=0&&end>start);
const code=html.slice(start,end),counts={1:4,2:4,3:7,4:6,5:6,6:6,7:6,8:6,9:7,10:14};
const source=fs.readFileSync(path.join(root,'books/AP_Textbook_Links_2026-27_Telugu-English.md'),'utf8');
const sourceUrls=[...source.matchAll(/\]\((https:\/\/cse\.ap\.gov\.in\/loadsupdocumentuploadbyid\?req_doc_id=[^)]+)\)/g)].map(m=>m[1]);
function setup(){
  const box={innerHTML:''},calls=[],opened=[],state={notes:[],files:[],requests:[]};
  const c={console,V:{},S:{cur:{c:7},bookPos:{}},param:{tab:'books',c:7},view:'library',CLASSES:Object.keys(counts).map(Number),SUBJ:{mat:{n:'గణితం'}},
    document:{getElementById:()=>box},window:{open:(...x)=>opened.push(x)},
    live:()=>state.notes,go:(...x)=>calls.push(x),pdfInit:()=>calls.push(['pdfInit']),
    esc:s=>String(s??'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;'),
    listDir:async(p,f)=>{state.requests.push([p,f]);return state.files;}};
  vm.createContext(c);vm.runInContext(code,c,{timeout:3000});
  return {c,box,calls,opened,state,get:expr=>JSON.parse(JSON.stringify(vm.runInContext(expr,c)))};
}
function hrefs(markup){return [...markup.matchAll(/href="([^"]*req_doc_id=2026-2027[^"]*)"/g)].map(m=>m[1]);}
function hrefs25(markup){return [...markup.matchAll(/href="([^"]*req_doc_id=2025-2026[^"]*)"/g)].map(m=>m[1]);}
async function run(){
  const f=setup(),all=[];
  for(const [grade,count] of Object.entries(counts)){
    f.c.param={tab:'books',c:+grade};f.c.S.cur.c=+grade;
    assert.ok(f.c.V.library().includes(`${grade}వ తరగతి`));
    await f.c.libLoad();const lib=f.get('LIB'),refs=lib.filter(x=>x.k==='aplink');
    assert.equal(refs.length,count);assert.equal(hrefs(f.box.innerHTML).length,count);
    assert.ok(f.box.innerHTML.includes('AP పుస్తకాల లింకులు — 2026–2027'));
    assert.ok(f.box.innerHTML.includes('ఇంటర్నెట్ అవసరం'));
    for(const r of refs){assert.ok(r.u.includes(`2026-2027${/2026-2027([WT])/.exec(r.u)[1]}${grade.padStart(2,'0')}`));all.push(r.u);}
    assert.ok(!f.box.innerHTML.includes('undefined'));
  }
  // 2025–26 గత సంవత్సరం లింకులు: అన్నీ view లో details లో; SEM2 view లో 2026–27 SEM2 లేనప్పుడు మాత్రమే.
  f.c.param={tab:'books',c:3};f.c.S.cur.c=3;await f.c.libLoad();assert.equal(hrefs25(f.box.innerHTML).length,13);
  f.c.param={tab:'books',c:3,sem:'2'};await f.c.libLoad();assert.equal(hrefs25(f.box.innerHTML).length,4);assert.ok(!f.box.innerHTML.includes('ఇంకా అధికారిక CSE పోర్టల్‌లో రాలేదు'));
  f.c.param={tab:'books',c:10,sem:'2'};f.c.S.cur.c=10;await f.c.libLoad();assert.equal(hrefs25(f.box.innerHTML).length,0);
  assert.deepEqual(all,sourceUrls);assert.equal(new Set(all).size,66);
  // Local PDFs, resume positions, and teacher-added books retain their old routes.
  f.c.param={tab:'books',c:7};f.c.S.cur.c=7;
  f.state.files=[{name:'Class7_Maths_SA1_Set1_Solutions_2026-27.pdf',size:25000}];
  f.state.notes=[{kind:'book',c:7,t:'టీచర్ పుస్తకం',url:'https://example.com/teacher.pdf',s:'mat'}];
  f.c.S.bookPos['books/7/Class7_Maths_SA1_Set1_Solutions_2026-27.pdf']=3;
  await f.c.libLoad();assert.equal(f.get('LIB').length,8);assert.ok(f.box.innerHTML.includes('పేజీ 3'));
  f.c.openItem(0);assert.equal(f.calls[0][0],'book');assert.equal(f.calls[0][1].k,'pdf');assert.equal(f.calls[1][0],'pdfInit');
  f.c.openItem(1);assert.equal(f.calls[2][1].u,'https://example.com/teacher.pdf');
  const apIndex=f.get("LIB.findIndex(x=>x.k==='aplink')");f.c.openItem(apIndex);
  assert.equal(f.opened[0][1],'_blank');assert.equal(f.opened[0][2],'noopener,noreferrer');
  assert.ok(f.box.innerHTML.includes('target="_blank" rel="noopener noreferrer"'));
  // AP catalog remains usable as a reference even if directory loading fails.
  f.state.files=null;f.state.notes=[];await f.c.libLoad(true);
  assert.equal(hrefs(f.box.innerHTML).length,6);assert.ok(f.box.innerHTML.includes('స్థానిక PDFల జాబితా ఇప్పుడు లోడ్ కాలేదు'));
  // Catalog appears immediately, before a slow GitHub/local-directory request finishes.
  const slow=setup(),resolvers=[];slow.c.listDir=(p)=>new Promise(resolve=>resolvers.push({p,resolve}));
  const first=slow.c.libLoad();assert.equal(hrefs(slow.box.innerHTML).length,6);assert.ok(slow.box.innerHTML.includes('లోడ్ అవుతోంది'));
  slow.c.param={tab:'books',c:8};slow.c.S.cur.c=8;const second=slow.c.libLoad();
  assert.ok(hrefs(slow.box.innerHTML).every(u=>u.includes('2026-2027T08')));
  resolvers[1].resolve([{name:'Class8_Test.pdf',size:100}]);await second;
  const latest=slow.box.innerHTML;resolvers[0].resolve([{name:'Class7_Stale.pdf',size:100}]);await first;
  assert.equal(slow.box.innerHTML,latest);assert.ok(!slow.box.innerHTML.includes('Class7'));
  // Tool tab is not polluted by textbook catalog, and keeps the old opening route.
  f.c.param={tab:'tools',c:7};f.state.files=[{name:'practice.html',size:30}];await f.c.libLoad();
  assert.equal(hrefs(f.box.innerHTML).length,0);assert.equal(f.get('LIB').length,1);f.c.openItem(0);
  assert.equal(f.calls.at(-1)[1].k,'tool');
  // Stored Google Apps Script payloads must stay byte-for-byte identical to branch base.
  const base=cp.execFileSync('git',['show','HEAD:index.html'],{cwd:root,encoding:'utf8',maxBuffer:16*1024*1024});
  for(const id of ['ms-code','gs-code']){
    const re=new RegExp(`<script[^>]*id=["']${id}["'][^>]*>([\\s\\S]*?)<\\/script>`,'i');
    const before=base.match(re),after=html.match(re);assert.ok(before&&after);assert.equal(after[1],before[1]);
  }
  console.log(JSON.stringify({status:'PASS',book_urls:66,classes:10,local_pdf_routes:'preserved',teacher_books:'preserved',tool_tab:'preserved',catalog_before_network:'PASS',offline_catalog:'PASS',class_switch_race:'PASS',new_tab_safety:'PASS',server_code:'unchanged',remote_pdf_downloads:'not tested'},null,2));
}
run().catch(e=>{console.error(e);process.exitCode=1;});
