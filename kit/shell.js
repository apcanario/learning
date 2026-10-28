(function(){
  // Panels carry their own context: data-ctx is the course id (or "root"), data-kind is root/course/syllabus/report,
  // and data-t / data-u / data-c give the top-bar title, label and colour. Report titles come from the drawer.
  var panels=[].slice.call(document.querySelectorAll('.panel'));
  var ids=panels.map(function(p){return p.id;});
  var ctxOf={},kindOf={},meta={},reportsBy={},courseName={};
  panels.forEach(function(p){
    var ctx=p.getAttribute('data-ctx')||'root',kind=p.getAttribute('data-kind')||'';
    ctxOf[p.id]=ctx;kindOf[p.id]=kind;
    if(p.hasAttribute('data-t'))meta[p.id]={t:p.getAttribute('data-t'),u:p.getAttribute('data-u')||'',c:p.getAttribute('data-c')||''};
    if(kind==='report')(reportsBy[ctx]=reportsBy[ctx]||[]).push(p.id);
    if(kind==='course')courseName[ctx]=p.getAttribute('data-t');
  });
  var items=[].slice.call(document.querySelectorAll('.ditem'));
  var navs=[].slice.call(document.querySelectorAll('[data-navctx]'));
  items.forEach(function(a){var un=a.closest('.dunit');if(!un)return;meta[a.getAttribute('data-target')]={t:a.querySelector('.t').textContent,n:a.querySelector('.n').textContent,u:un.getAttribute('data-ulabel'),c:un.style.getPropertyValue('--c')};});
  function isReport(id){return kindOf[id]==='report';}
  function seqFor(ctx){return ids.filter(function(i){return ctxOf[i]===ctx;});}
  // KEY keeps the last report read in any course (the name predates the second course); LKEY+ctx the last per course.
  var KEY='hellas-reports-tab', LKEY='pm-last-', UKEY='hellas-units-open';
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

  // unit collapse: closed by default; remember which the reader opened (keys are namespaced per course)
  var opened={};try{opened=JSON.parse(get(UKEY)||'{}')||{};}catch(e){}
  [].slice.call(document.querySelectorAll('.dunit')).forEach(function(un){
    var u=un.getAttribute('data-unit');var h=un.querySelector('.duh');
    if(opened[u]){un.classList.remove('closed');h.setAttribute('aria-expanded','true');}
    h.addEventListener('click',function(){var c=un.classList.toggle('closed');h.setAttribute('aria-expanded',c?'false':'true');if(c)delete opened[u];else opened[u]=1;put(UKEY,JSON.stringify(opened));});
  });

  function lastAny(){var s=get(KEY);return s&&isReport(s)&&meta[s]?s:null;}
  function lastIn(ctx){var s=get(LKEY+ctx);if(s&&isReport(s)&&ctxOf[s]===ctx&&meta[s])return s;s=lastAny();return s&&ctxOf[s]===ctx?s:null;}

  function show(id,scroll){
    if(ids.indexOf(id)<0)id='home';
    current=id;var ctx=ctxOf[id];
    panels.forEach(function(p){p.hidden=p.id!==id;});
    navs.forEach(function(n){n.hidden=n.getAttribute('data-navctx')!==ctx;});
    items.forEach(function(a){var on=a.getAttribute('data-target')===id;a.classList.toggle('is-active',on);if(on)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current');
      if(on){var un=a.closest('.dunit');if(un&&un.classList.contains('closed')){un.classList.remove('closed');un.querySelector('.duh').setAttribute('aria-expanded','true');}}});
    var m=meta[id]||{};
    curFull=m.n?(m.u||'')+' · '+m.n:(m.u||'');fitCur();curT.textContent=m.t||'';cur.style.setProperty('--c',m.c||'');
    homeB.classList.toggle('is-here',id==='home');
    if(id==='home')homeB.setAttribute('aria-current','page');else homeB.removeAttribute('aria-current');
    var seq=seqFor(ctx),k=seq.indexOf(id);
    arrows.hidden=seq.length<2||ctx==='root';
    prevB.disabled=k<=0;nextB.disabled=k>=seq.length-1;
    var pg=document.querySelector('#'+id+' .pager');
    if(pg&&!pg.innerHTML){
      var rs=reportsBy[ctx]||[],r=rs.indexOf(id),h='';
      if(r>0){var p=meta[rs[r-1]];h+='<a href="#'+rs[r-1]+'" class="prev"><span>'+p.n+'</span>'+p.t+'</a>';}
      if(r>=0&&r<rs.length-1){var n=meta[rs[r+1]];h+='<a href="#'+rs[r+1]+'" class="next">'+n.t+'<span>'+n.n+'</span></a>';}
      pg.innerHTML=h;
    }
    if(isReport(id)){put(KEY,id);put(LKEY+ctx,id);}
    updateContinue();
    if(scroll)window.scrollTo(0,0);
  }
  // on each course home, open the unit card holding that course's last report (or the first card), once
  function openCards(){
    [].slice.call(document.querySelectorAll('.panel[data-kind="course"]')).forEach(function(home){
      var ctx=home.getAttribute('data-ctx'),s=lastIn(ctx)||(reportsBy[ctx]||[])[0];
      var cards=[].slice.call(home.querySelectorAll('details.ucard')),hit=null;
      if(s)cards.forEach(function(c){if((' '+c.getAttribute('data-mods')+' ').indexOf(' '+s+' ')>=0)hit=c;});
      if(!hit)hit=cards[0];
      if(hit&&!hit.dataset.auto){hit.open=true;hit.dataset.auto='1';}
    });
  }
  // continue buttons: the root one (data-long) resumes any course and names it; a course one resumes within its course
  function updateContinue(){
    [].slice.call(document.querySelectorAll('.hbtn.cont')).forEach(function(b){
      var long=b.hasAttribute('data-long'),s=long?lastAny():lastIn(b.getAttribute('data-course'));
      var t=b.querySelector('b');
      if(s){b.hidden=false;b.href='#'+s;b.setAttribute('data-target',s);t.textContent=(long?(courseName[ctxOf[s]]||'')+' · ':'')+meta[s].n+' '+meta[s].t;}
      else{b.hidden=true;}
      // "Start the course" shows only while there is nothing to continue; data-one when a single button is left
      var st=b.parentNode.querySelector('.hbtn.start');if(st)st.hidden=!!s;
      var vis=[].filter.call(b.parentNode.querySelectorAll('.hbtn'),function(x){return !x.hidden;}).length;
      if(vis===1)b.parentNode.setAttribute('data-one','');else b.parentNode.removeAttribute('data-one');
    });
    openCards();}
  function go(id){history.replaceState(null,'','#'+id);show(id,true);}
  prevB.addEventListener('click',function(){var seq=seqFor(ctxOf[current]),k=seq.indexOf(current);if(k>0)go(seq[k-1]);});
  nextB.addEventListener('click',function(){var seq=seqFor(ctxOf[current]),k=seq.indexOf(current);if(k<seq.length-1)go(seq[k+1]);});
  homeB.addEventListener('click',function(e){e.preventDefault();go('home');});
  [].slice.call(document.querySelectorAll('[data-target]:not(.ditem)')).forEach(function(a){a.addEventListener('click',function(e){var t=a.getAttribute('data-target');if(!t)return;e.preventDefault();go(t);});});
  // a drawer item without data-target is an external link (a markdown course's own artifact until A3): the browser follows it
  items.forEach(function(a){a.addEventListener('click',function(e){var t=a.getAttribute('data-target');if(!t){closeDrawer();return;}e.preventDefault();closeDrawer();go(t);});});

  var themeB=document.getElementById('themeB');
  function effTheme(){var d=document.documentElement.getAttribute('data-theme');if(d==='light'||d==='dark')return d;return (window.matchMedia&&window.matchMedia('(prefers-color-scheme: light)').matches)?'light':'dark';}
  themeB.addEventListener('click',function(){var next=effTheme()==='dark'?'light':'dark';document.documentElement.setAttribute('data-theme',next);put('hellas-theme',next);});

  [].slice.call(document.querySelectorAll('.copy')).forEach(function(bt){
    bt.addEventListener('click',function(){var pre=bt.closest('.pbox').querySelector('pre');var txt=pre.textContent;
      function ok(){bt.textContent='copied';bt.classList.add('ok');setTimeout(function(){bt.textContent='copy prompt';bt.classList.remove('ok');},1600);}
      function fb(){try{var r=document.createRange();r.selectNodeContents(pre);var s=window.getSelection();s.removeAllRanges();s.addRange(r);bt.textContent='selected, copy manually';}catch(e){}}
      if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(txt).then(ok,fb);}else{fb();}});
  });

  function route(){
    var h=(location.hash||'').slice(1);
    if(h==='next')h='home';
    if(!h){show('home',false);return;}
    if(ids.indexOf(h)>=0){show(h,true);return;}
    var el=document.getElementById(h);
    if(el){var p=el.closest('.panel');if(p){show(p.id,false);setTimeout(function(){el.scrollIntoView();},0);return;}}
    show('home',false);
  }
  window.addEventListener('hashchange',route);
  route();
})();
