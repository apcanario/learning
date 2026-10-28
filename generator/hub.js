(function(){
  // Hub shell, modelled on Personal Mythology's shell.js: hash-routed panels (.panel, one visible),
  // a slide-out drawer, top-bar context, theme toggle, copy buttons. Adds the hub's back navigation:
  // a page history inside the hub (back button) and swipe from the left edge.
  var root=document.documentElement, KEY=root.getAttribute('data-theme-key')||'hub-theme';
  var panels=[].slice.call(document.querySelectorAll('.panel'));
  var ids=panels.map(function(p){return p.id;});
  var items=[].slice.call(document.querySelectorAll('.ditem[data-target]'));
  var drawer=document.getElementById('drawer'),backdrop=document.getElementById('backdrop'),menuB=document.getElementById('menuB'),closeB=document.getElementById('closeB');
  var backB=document.getElementById('backB'),homeB=document.getElementById('homeB'),themeB=document.getElementById('themeB');
  var cur=document.getElementById('cur'),curU=document.getElementById('curU'),curT=document.getElementById('curT');
  function get(k){try{return localStorage.getItem(k);}catch(e){return null;}}
  function put(k,v){try{localStorage.setItem(k,v);}catch(e){}}

  function openDrawer(){drawer.classList.add('on');backdrop.classList.add('on');drawer.setAttribute('aria-hidden','false');menuB.setAttribute('aria-expanded','true');root.classList.add('locked');closeB.focus();}
  function closeDrawer(){drawer.classList.remove('on');backdrop.classList.remove('on');drawer.setAttribute('aria-hidden','true');menuB.setAttribute('aria-expanded','false');root.classList.remove('locked');}
  menuB.addEventListener('click',openDrawer);
  closeB.addEventListener('click',function(){closeDrawer();menuB.focus();});
  backdrop.addEventListener('click',closeDrawer);
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&drawer.classList.contains('on')){closeDrawer();menuB.focus();}});

  // top-bar context stays on one line; shortened only when the bar is too narrow
  var full='';
  function fit(){curU.textContent=full;if(curU.scrollWidth>curU.clientWidth)curU.textContent=full.replace(/^[^·]+· /,'');}
  window.addEventListener('resize',fit);
  try{document.fonts.ready.then(fit);}catch(e){}

  var current=null,stack=[];
  function show(id,scroll){
    if(ids.indexOf(id)<0)id='home';
    current=id;
    var p=document.getElementById(id);
    panels.forEach(function(x){x.hidden=x.id!==id;});
    var act=p.getAttribute('data-nav')||id;
    items.forEach(function(a){var on=a.getAttribute('data-target')===act;a.classList.toggle('is-active',on);if(on)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current');});
    full=p.getAttribute('data-u')||'';fit();curT.textContent=p.getAttribute('data-t')||'';cur.style.setProperty('--c',p.getAttribute('data-c')||'');
    homeB.classList.toggle('is-here',id==='home');
    backB.disabled=(stack.length===0&&id==='home');
    if(scroll)window.scrollTo(0,0);
  }
  function panelOf(h){if(ids.indexOf(h)>=0)return h;var el=h&&document.getElementById(h);var p=el&&el.closest('.panel');return p?p.id:null;}
  var skip=false,last=null;
  function route(){
    var h=(location.hash||'').slice(1)||'home',pid=panelOf(h)||'home';
    if(!skip&&last&&pid!==last)stack.push(last);
    skip=false;
    if(pid===h)show(pid,true);
    else{show(pid,false);var el=document.getElementById(h);setTimeout(function(){el.scrollIntoView();},0);}
    last=pid;closeDrawer();
  }
  function back(){
    if(stack.length){skip=true;location.hash='#'+stack.pop();}
    else if(current!=='home'){skip=true;location.hash='#home';}
  }
  backB.addEventListener('click',back);
  window.addEventListener('hashchange',route);
  // swipe from the left edge goes back (the drawer opens from the menu button only)
  var sx=null,sy=0,edge=false;
  document.addEventListener('touchstart',function(e){var t=e.touches[0];sx=t.clientX;sy=t.clientY;edge=sx<28&&!drawer.classList.contains('on');},{passive:true});
  document.addEventListener('touchend',function(e){if(!edge||sx===null)return;var t=e.changedTouches[0];if(t.clientX-sx>80&&Math.abs(t.clientY-sy)<60)back();sx=null;edge=false;},{passive:true});

  function eff(){var d=root.getAttribute('data-theme');if(d==='light'||d==='dark')return d;return (window.matchMedia&&window.matchMedia('(prefers-color-scheme: light)').matches)?'light':'dark';}
  themeB.addEventListener('click',function(){var n=eff()==='dark'?'light':'dark';root.setAttribute('data-theme',n);put(KEY,n);});

  [].slice.call(document.querySelectorAll('.copy')).forEach(function(bt){
    var label=bt.textContent;
    bt.addEventListener('click',function(){var pre=bt.closest('.pbox').querySelector('pre');var txt=pre.textContent;
      function ok(){bt.textContent='copied';bt.classList.add('ok');setTimeout(function(){bt.textContent=label;bt.classList.remove('ok');},1600);}
      function fb(){try{var r=document.createRange();r.selectNodeContents(pre);var s=window.getSelection();s.removeAllRanges();s.addRange(r);bt.textContent='selected, copy manually';}catch(e){}}
      if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(txt).then(ok,fb);}else{fb();}});
  });
  route();
})();
