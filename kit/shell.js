(function(){
  // Panels carry their own context: data-ctx is the course id (or "root"), data-kind is root/course/syllabus/report,
  // and data-t / data-u / data-c give the top-bar title, label and colour. Report titles come from the drawer.
  // A report panel arrives as an empty stub with data-src, its file's path relative to this page (docs/academy.md A2),
  // and so do the syllabi and a markdown course's briefs and bibliography pages (P20) and the history course homes
  // (P22): the first visit fetches the file into the panel, which keeps it for the rest of the visit (data-loaded).
  // A stub that is not a report lists the ids inside its file in data-anchors, so a link to one of them loads the
  // panel first. Clicks and copy buttons are delegated, so content that arrives by fetch works like content that was
  // in the page.
  var panels=[].slice.call(document.querySelectorAll('.panel'));
  var ids=panels.map(function(p){return p.id;});
  var ctxOf={},kindOf={},meta={},reportsBy={};
  panels.forEach(function(p){
    var ctx=p.getAttribute('data-ctx')||'root',kind=p.getAttribute('data-kind')||'';
    ctxOf[p.id]=ctx;kindOf[p.id]=kind;
    if(p.hasAttribute('data-t'))meta[p.id]={t:p.getAttribute('data-t'),u:p.getAttribute('data-u')||'',c:p.getAttribute('data-c')||''};
    if(kind==='report')(reportsBy[ctx]=reportsBy[ctx]||[]).push(p.id);
  });
  var items=[].slice.call(document.querySelectorAll('.ditem'));
  var navs=[].slice.call(document.querySelectorAll('[data-navctx]'));
  items.forEach(function(a){var un=a.closest('.dunit');if(!un||meta[a.getAttribute('data-target')])return;meta[a.getAttribute('data-target')]={t:a.querySelector('.t').textContent,n:a.querySelector('.n').textContent,u:un.getAttribute('data-ulabel'),c:un.style.getPropertyValue('--c')};});
  function isReport(id){return kindOf[id]==='report';}
  function seqFor(ctx){return ids.filter(function(i){return ctxOf[i]===ctx;});}
  // KEY keeps the last report read in any course (the name predates the second course); LKEY+ctx the last per course.
  var KEY='__STORE_TAB__', LKEY='__STORE_LAST__', UKEY='__STORE_UNITS__';
  var drawer=document.getElementById('drawer'),backdrop=document.getElementById('backdrop'),menuB=document.getElementById('menuB'),closeB=document.getElementById('closeB'),prevB=document.getElementById('prevB'),nextB=document.getElementById('nextB'),homeB=document.getElementById('homeB'),arrows=document.getElementById('arrows');
  var curU=document.getElementById('curU'),curT=document.getElementById('curT'),cur=document.getElementById('cur');
  var current=null;
  // top-bar context stays on one line: full "ROME · UNIT 1 · 1.2", shortened to "U1" only when the bar is too narrow
  var curFull='';
  function fitCur(){curU.textContent=curFull;if(curU.scrollWidth>curU.clientWidth)curU.textContent=curFull.replace('UNIT ','U');}
  window.addEventListener('resize',fitCur);
  try{document.fonts.ready.then(fitCur);}catch(e){}
  function get(k){try{return localStorage.getItem(k);}catch(e){return null;}}
  function put(k,v){try{localStorage.setItem(k,v);}catch(e){}}

  function openDrawer(){drawer.classList.add('on');backdrop.classList.add('on');drawer.setAttribute('aria-hidden','false');menuB.setAttribute('aria-expanded','true');document.documentElement.classList.add('locked');
    var act=drawer.querySelector('[data-navctx]:not([hidden]) .ditem.is-active');if(act){try{act.scrollIntoView({block:'center'});}catch(e){}}
    closeB.focus();}
  function closeDrawer(){drawer.classList.remove('on');backdrop.classList.remove('on');drawer.setAttribute('aria-hidden',(wide&&wide.matches)?'false':'true');menuB.setAttribute('aria-expanded','false');document.documentElement.classList.remove('locked');}
  menuB.addEventListener('click',openDrawer);
  closeB.addEventListener('click',function(){closeDrawer();menuB.focus();});
  backdrop.addEventListener('click',closeDrawer);
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&drawer.classList.contains('on')){closeDrawer();menuB.focus();}});
  // desktop (theme.css section 6): the drawer is a persistent sidebar, so it is never "closed" or hidden to assistive tech
  var wide=window.matchMedia?window.matchMedia('(min-width:1100px)'):null;
  function syncWide(){if(!wide)return;if(wide.matches){closeDrawer();drawer.setAttribute('aria-hidden','false');}}
  if(wide){if(wide.addEventListener)wide.addEventListener('change',syncWide);else if(wide.addListener)wide.addListener(syncWide);syncWide();}

  // collapsible groups in the drawer (.dunit): a course's units are an accordion, one open at a time, closed by
  // default; the root tracks are independent and open by default. The reader's choice is remembered per group
  // (1 open, 0 closed; keys are namespaced per course).
  var opened={};try{opened=JSON.parse(get(UKEY)||'{}')||{};}catch(e){}
  function setOpen(un,on){un.classList.toggle('closed',!on);un.querySelector('.duh').setAttribute('aria-expanded',on?'true':'false');}
  function openGroup(un,remember){
    var nav=un.closest('[data-navctx]');
    if(nav&&nav.hasAttribute('data-accordion'))[].slice.call(nav.querySelectorAll('.dunit')).forEach(function(o){if(o!==un&&!o.classList.contains('closed')){setOpen(o,false);if(remember)opened[o.getAttribute('data-unit')]=0;}});
    setOpen(un,true);if(remember)opened[un.getAttribute('data-unit')]=1;
    if(remember)put(UKEY,JSON.stringify(opened));
  }
  [].slice.call(document.querySelectorAll('.dunit')).forEach(function(un){
    var u=un.getAttribute('data-unit');var h=un.querySelector('.duh');
    var dflt=un.hasAttribute('data-open'),st=opened[u];
    setOpen(un,st===1||(st===undefined&&dflt));
    h.addEventListener('click',function(){if(un.classList.contains('closed'))openGroup(un,true);else{setOpen(un,false);opened[u]=0;put(UKEY,JSON.stringify(opened));}});
  });
  // an accordion keeps one group open: the stored state may hold several from before, so keep only the first
  navs.forEach(function(n){if(!n.hasAttribute('data-accordion'))return;var open=[].slice.call(n.querySelectorAll('.dunit:not(.closed)'));open.slice(1).forEach(function(o){setOpen(o,false);});});
  // the root tracks start closed; with no remembered choice, the track of the last report read opens (else the first)
  (function(){var root=document.querySelector('[data-navctx="root"]');if(!root)return;
    var groups=[].slice.call(root.querySelectorAll('.dunit'));if(!groups.length||groups.some(function(g){return opened[g.getAttribute('data-unit')]!==undefined;}))return;
    var s=lastAny(),hit=null;if(s){var a=root.querySelector('.ditem[data-target="'+ctxOf[s]+'"]');if(a)hit=a.closest('.dunit');}
    setOpen(hit||groups[0],true);})();

  // figure frames (P44, 29 Oct 2026): below 768 px a figure keeps its natural size and scrolls sideways in its .viz-scroll
  // frame; data-more names the edge(s) with more drawing (the theme fades them) and the cue line under the frame shows
  // only while the drawing is wider than the frame. Run when a panel is shown, when a fetched panel lands, when a
  // <details> opens and on resize; a hidden frame measures 0 and so carries no cue until it is shown.
  function vizEdge(f){var sw=f.scrollWidth,cw=f.clientWidth,l=f.scrollLeft>(+f.getAttribute('data-x0px')||0)+1,r=f.scrollLeft+cw<sw-1,m=(l?'l':'')+(r?'r':'');
    if(m)f.setAttribute('data-more',m);else f.removeAttribute('data-more');}
  // P68: a wide table's frame (.tbl) gets the same fade and cue, so a reader knows it scrolls
  function vizFrames(root){if(!root)return;[].slice.call(root.querySelectorAll('.viz-scroll, .report .tbl')).forEach(function(f){
    var cue=f.nextElementSibling;
    if(!cue||!cue.classList.contains('viz-cue')){cue=document.createElement('p');cue.className='viz-cue';cue.textContent='scroll sideways for the whole '+(f.classList.contains('tbl')?'table':'figure');f.parentNode.insertBefore(cue,f.nextSibling);}
    if(!f.hasAttribute('data-sc')){f.setAttribute('data-sc','');f.addEventListener('scroll',function(){vizEdge(f);},{passive:true});}
    var over=f.clientWidth>0&&f.scrollWidth>f.clientWidth+1;cue.hidden=!over;
    // P58: a drawing centred in a wider svg (a narrow tree) names where it starts (data-x0); on its first measured
    // showing a scrolling frame opens there, not on the empty margin; P50: the left fade shows only past that point, since
    // to its left there is margin, not drawing
    // P79: a tree also names its root's right edge (data-xr); the frame opens no further left than puts it in view
    var sv=f.querySelector('svg[data-x0], svg[data-xr]');if(over&&sv&&!f.hasAttribute('data-x0done')){f.setAttribute('data-x0done','');
      var vb=sv.viewBox&&sv.viewBox.baseVal,k=vb&&vb.width?sv.getBoundingClientRect().width/vb.width:1,a=Math.max(0,(+sv.getAttribute('data-x0')||0)*k-12);
      f.scrollLeft=Math.max(a,(+sv.getAttribute('data-xr')||0)*k-f.clientWidth);f.setAttribute('data-x0px',a);}
    vizEdge(f);});}
  window.addEventListener('resize',function(){vizFrames(document.querySelector('.panel:not([hidden])'));});
  document.addEventListener('toggle',function(e){if(e.target&&e.target.querySelector)vizFrames(e.target);},true);
  // P68 · the reading layout (1 Nov 2026). A unit or report (built by mdcourse.reading) reads one section at a time:
  // .report.steps holds one .sec per h2; the sticky .stepbar shows "Section n of N", the progress bar, the section
  // menu and the "Whole unit" toggle. The section last read is kept per page (SKEY+id), so Continue, a drawer item or a
  // reload reopens it there. A link to an id inside the page (the menu, a section's next and previous, a deep link
  // #m54-3, a link into the Sources or "How this unit was made" accordion) shows that section or opens that accordion
  // first, then scrolls to it. "Whole unit" shows every section for search and print; the bar then follows the scroll.
  var SKEY='__STORE_SECTION__';
  function stepsOf(p){var r=p&&p.querySelector('.report.steps');return r?[].slice.call(r.children).filter(function(s){return s.classList.contains('sec');}):[];}
  function isWhole(p){var r=p&&p.querySelector('.report.steps');return !!r&&r.classList.contains('whole');}
  function initSteps(p){
    var r=p&&p.querySelector('.report.steps');if(!r||r.hasAttribute('data-ready'))return;
    r.setAttribute('data-ready','');r.classList.add('stepping');
    var k=parseInt(get(SKEY+p.id),10),n=stepsOf(p).length;if(!(k>=0&&k<n))k=0;
    setStep(p,k,false);}
  function barState(p,k){
    var bar=p.querySelector('.stepbar');if(!bar)return;var n=+bar.getAttribute('data-n')||1;
    var links=[].slice.call(bar.querySelectorAll('.seclist a'));
    bar.querySelector('.sof b').textContent=k+1;
    links.forEach(function(a,i){if(i===k)a.setAttribute('aria-current','step');else a.removeAttribute('aria-current');});
    var tt=links[k]&&links[k].querySelector('.t');bar.querySelector('.stt').textContent=tt?tt.textContent:'';
    bar.querySelector('.sprog i').style.width=(100*(k+1)/n).toFixed(2)+'%';
    p.setAttribute('data-step',k);
    // the process accordions and the next unit show at the end of the last section (or when a link opens them)
    if(k===n-1||isWhole(p))p.setAttribute('data-end','');else p.removeAttribute('data-end');}
  function setStep(p,k,scroll){
    var secs=stepsOf(p);if(!secs.length)return;k=Math.max(0,Math.min(secs.length-1,k));
    if(!isWhole(p))secs.forEach(function(s,i){s.classList.toggle('on',i===k);});
    barState(p,k);put(SKEY+p.id,String(k));
    vizFrames(secs[k]);
    if(scroll){if(k===0&&!isWhole(p))window.scrollTo(0,0);else{var h=secs[k].querySelector('h2.band')||secs[k];h.scrollIntoView();}}}
  function setWhole(p,on){
    var r=p.querySelector('.report.steps'),b=p.querySelector('.stepbar .whole');if(!r)return;
    var k=+(p.getAttribute('data-step')||0),secs=stepsOf(p);
    r.classList.toggle('whole',on);if(b)b.setAttribute('aria-pressed',on?'true':'false');
    var mn=p.querySelector('.secmenu[open]');if(mn)mn.open=false;if(on)p.setAttribute('data-end','');
    if(on){secs.forEach(function(s){s.classList.add('on');});vizFrames(r);if(k>0)(secs[k].querySelector('h2.band')||secs[k]).scrollIntoView();}
    else{k=inView(p);setStep(p,k,true);}}
  // the section whose band is the last one above the bar's lower edge
  function inView(p){var secs=stepsOf(p),bar=p.querySelector('.stepbar'),y=(bar?bar.getBoundingClientRect().bottom:0)+40,k=0;
    secs.forEach(function(s,i){if(s.getBoundingClientRect().top<=y)k=i;});return k;}
  window.addEventListener('scroll',function(){var p=current&&document.getElementById(current);
    if(p&&isWhole(p)){var k=inView(p);if(k!==+p.getAttribute('data-step')){barState(p,k);put(SKEY+p.id,String(k));}}},{passive:true});
  // show what an id inside a reading page sits in (its section, the accordions round it), then scroll to it
  function reveal(el){
    var p=el.closest('.panel'),sec=el.closest('.sec');
    if(p&&sec&&!isWhole(p)){var k=stepsOf(p).indexOf(sec);if(k>=0&&!sec.classList.contains('on'))setStep(p,k,false);}
    if(p&&el.closest('.process'))p.setAttribute('data-end','');
    for(var d=el.closest('details');d;d=d.parentElement&&d.parentElement.closest('details'))d.open=true;
    var m=p&&p.querySelector('.secmenu[open]');if(m)m.open=false;
    el.scrollIntoView();}
  document.addEventListener('click',function(e){
    if(e.defaultPrevented||e.button||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey)return;
    var b=e.target.closest&&e.target.closest('.stepbar .whole');
    if(b){var pw=b.closest('.panel');setWhole(pw,!isWhole(pw));return;}
    var a=e.target.closest&&e.target.closest('a[href^="#"]');if(!a||a.hasAttribute('data-target'))return;
    var p=a.closest('.panel[data-kind="report"]');if(!p)return;
    var el=document.getElementById(a.getAttribute('href').slice(1));if(!el||!p.contains(el))return;
    e.preventDefault();
    if(a.hasAttribute('data-step')){var mm=p.querySelector('.secmenu[open]');if(mm)mm.open=false;
      if(isWhole(p))reveal(el);else setStep(p,+a.getAttribute('data-step'),true);}
    else reveal(el);});
  // a click outside an open section menu closes it
  document.addEventListener('click',function(e){var m=document.querySelector('.panel:not([hidden]) .secmenu[open]');if(m&&!m.contains(e.target))m.open=false;});
  function lastAny(){var s=get(KEY);return s&&isReport(s)&&meta[s]?s:null;}
  function lastIn(ctx){var s=get(LKEY+ctx);if(s&&isReport(s)&&ctxOf[s]===ctx&&meta[s])return s;s=lastAny();return s&&ctxOf[s]===ctx?s:null;}

  function show(id,scroll){
    if(ids.indexOf(id)<0)id='home';
    current=id;var ctx=ctxOf[id];
    panels.forEach(function(p){p.hidden=p.id!==id;});
    vizFrames(document.getElementById(id));
    navs.forEach(function(n){n.hidden=n.getAttribute('data-navctx')!==ctx;});
    items.forEach(function(a){var on=a.getAttribute('data-target')===id;a.classList.toggle('is-active',on);if(on)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current');
      if(on){var un=a.closest('.dunit');if(un&&un.classList.contains('closed'))openGroup(un,false);}});
    var m=meta[id]||{};
    curFull=m.n?(m.u||'')+' · '+m.n:(m.u||'');fitCur();curT.textContent=m.t||'';cur.style.setProperty('--c',m.c||'');
    homeB.classList.toggle('is-here',id==='home');
    if(id==='home')homeB.setAttribute('aria-current','page');else homeB.removeAttribute('aria-current');
    var seq=seqFor(ctx),k=seq.indexOf(id);
    arrows.hidden=seq.length<2||ctx==='root';
    prevB.disabled=k<=0;nextB.disabled=k>=seq.length-1;
    if(isReport(id)){put(KEY,id);put(LKEY+ctx,id);}
    updateContinue();
    if(scroll)window.scrollTo(0,0);
    var done=load(id);
    // a fetched panel's continue button and unit cards (a course home, P22) only exist once its file has landed
    done.then(function(ok){if(ok&&current===id){initSteps(document.getElementById(id));pager(id);prefetch(id);if(kindOf[id]==='course')updateContinue();}});
    return done;
  }
  function pager(id){
    var pg=document.querySelector('#'+id+' .pager');
    if(pg&&!pg.innerHTML){
      var ctx=ctxOf[id],rs=reportsBy[ctx]||[],r=rs.indexOf(id),h='';
      // P68: each card says which way it goes, then the code and the title
      if(r>0){var p=meta[rs[r-1]];h+='<a href="#'+rs[r-1]+'" class="prev"><span>Previous unit'+(p.n?' · '+p.n:'')+'</span><b>'+p.t+'</b></a>';}
      if(r>=0&&r<rs.length-1){var n=meta[rs[r+1]];h+='<a href="#'+rs[r+1]+'" class="next"><span>Next unit'+(n.n?' · '+n.n:'')+'</span><b>'+n.t+'</b></a>';}
      pg.innerHTML=h;
    }
  }
  // fetch a panel's file into its stub; resolves true when the panel holds its content (at once for a panel in the page)
  var loading={};
  function load(id){
    var p=document.getElementById(id),src=p&&p.getAttribute('data-src');
    if(!src||p.hasAttribute('data-loaded'))return Promise.resolve(true);
    if(loading[id])return loading[id];
    if(!p.innerHTML||p.hasAttribute('data-failed'))p.innerHTML='<p class="hnote">Loading…</p>';
    p.removeAttribute('data-failed');
    loading[id]=fetch(src).then(function(r){if(!r.ok)throw new Error('HTTP '+r.status);return r.text();}).then(function(t){
      p.innerHTML=t;p.setAttribute('data-loaded','');p.removeAttribute('data-failed');delete loading[id];vizFrames(p);return true;
    },function(err){
      delete loading[id];p.setAttribute('data-failed','');
      var m=meta[id]||{},esc=function(x){return String(x).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});};
      p.innerHTML='<header class="phead"><h1>'+esc(m.t||'This page')+'</h1></header><p class="prov flag">The page could not be loaded ('+esc(err&&err.message||'network error')+'). Check the connection and try again.</p><div class="hlinks" data-one><a class="hbtn alt" href="#'+id+'" data-target="'+id+'"><span>Try again</span><b>'+esc((m.n?m.n+' ':'')+(m.t||''))+'</b></a></div>';
      return false;
    });
    return loading[id];
  }
  // the next report in the course is fetched in the background, so turning the page does not wait
  function prefetch(id){
    var rs=reportsBy[ctxOf[id]]||[],r=rs.indexOf(id);
    if(r<0||r>=rs.length-1)return;
    setTimeout(function(){load(rs[r+1]);},400);
  }
  // on each course home, open the unit card holding that course's last report (or the first card), once
  function openCards(){
    [].slice.call(document.querySelectorAll('.panel[data-kind="course"]')).forEach(function(home){
      var ctx=home.getAttribute('data-ctx'),s=lastIn(ctx)||(reportsBy[ctx]||[])[0];
      var cards=[].slice.call(home.querySelectorAll('details[data-mods]')),hit=null;   // P93: a history unit's tile, the summary of its disclosure
      if(s)cards.forEach(function(c){if((' '+c.getAttribute('data-mods')+' ').indexOf(' '+s+' ')>=0)hit=c;});
      if(!hit)hit=cards[0];
      if(hit&&!hit.dataset.auto){hit.open=true;hit.dataset.auto='1';}
    });
  }
  // continue buttons: each course home's resumes within its course (P91, 4 Nov 2026: the home has none; Pedro: one
  // state across every course is "kind of useless until we create a login system")
  function updateContinue(){
    [].slice.call(document.querySelectorAll('.hbtn.cont')).forEach(function(b){
      var s=lastIn(b.getAttribute('data-course'));
      var t=b.querySelector('b');
      if(s){b.hidden=false;b.href='#'+s;b.setAttribute('data-target',s);t.textContent=(meta[s].n?meta[s].n+' ':'')+meta[s].t;}
      else{b.hidden=true;}
      // the course's Start button shows only while there is nothing to continue; data-one when a single button is left
      var st=b.parentNode.querySelector('.hbtn.start');if(st)st.hidden=!!s;
      var vis=[].filter.call(b.parentNode.querySelectorAll('.hbtn'),function(x){return !x.hidden;}).length;
      if(vis===1)b.parentNode.setAttribute('data-one','');else b.parentNode.removeAttribute('data-one');
    });
    openCards();}
  // P91: a target that is not a panel but an id inside one (a shelf spine's #greece-u3, a unit's breadcrumb) is routed
  // as a link to it would be: its panel is shown (fetched first if need be) and the id revealed
  function go(id){history.replaceState(null,'','#'+id);if(ids.indexOf(id)<0){route();return;}show(id,true);}
  prevB.addEventListener('click',function(){var seq=seqFor(ctxOf[current]),k=seq.indexOf(current);if(k>0)go(seq[k-1]);});
  nextB.addEventListener('click',function(){var seq=seqFor(ctxOf[current]),k=seq.indexOf(current);if(k<seq.length-1)go(seq[k+1]);});
  homeB.addEventListener('click',function(e){e.preventDefault();go('home');});
  document.addEventListener('click',function(e){
    if(e.defaultPrevented||e.button||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey)return;
    var a=e.target.closest&&e.target.closest('[data-target]');if(!a||a.classList.contains('ditem'))return;
    var t=a.getAttribute('data-target');if(!t)return;e.preventDefault();go(t);});
  items.forEach(function(a){a.addEventListener('click',function(e){var t=a.getAttribute('data-target');if(!t){closeDrawer();return;}e.preventDefault();closeDrawer();go(t);});});

  var themeB=document.getElementById('themeB');
  function effTheme(){var d=document.documentElement.getAttribute('data-theme');if(d==='light'||d==='dark')return d;return (window.matchMedia&&window.matchMedia('(prefers-color-scheme: light)').matches)?'light':'dark';}
  themeB.addEventListener('click',function(){var next=effTheme()==='dark'?'light':'dark';document.documentElement.setAttribute('data-theme',next);put('__STORE_THEME__',next);});

  document.addEventListener('click',function(e){
    var bt=e.target.closest&&e.target.closest('.copy');if(!bt||bt.classList.contains('ok'))return;
    var pre=bt.closest('.pbox').querySelector('pre');var txt=pre.textContent;
    var was=bt.textContent;
    function ok(){bt.textContent='copied';bt.classList.add('ok');setTimeout(function(){bt.textContent=was;bt.classList.remove('ok');},1600);}
    function fb(){try{var r=document.createRange();r.selectNodeContents(pre);var s=window.getSelection();s.removeAllRanges();s.addRange(r);bt.textContent='selected, copy manually';}catch(e){}}
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(txt).then(ok,fb);}else{fb();}});

  function route(){
    var h=(location.hash||'').slice(1);
    if(h==='next')h='home';
    if(!h){show('home',false);return;}
    if(ids.indexOf(h)>=0){show(h,true);return;}
    var el=document.getElementById(h);
    if(el){var p=el.closest('.panel');if(p){show(p.id,false).then(function(){if(current===p.id)reveal(el);});return;}}
    // an id inside a file not yet fetched: a report section (#m23-2) by its numbering, its accordions (#m23-sources,
    // #m23-made, P68; #m23-note, P73) by their suffix, any other (#rs-u3) by data-anchors
    var pid=h.replace(/-(\d+|sources|made|note)$/,'');
    if(pid===h||!isReport(pid)){pid=null;panels.some(function(p){if((' '+(p.getAttribute('data-anchors')||'')+' ').indexOf(' '+h+' ')>=0){pid=p.id;return true;}});}
    if(pid){show(pid,false).then(function(){var t=document.getElementById(h);if(t&&current===pid)reveal(t);});return;}
    show('home',false);
  }
  window.addEventListener('hashchange',route);
  route();
})();
