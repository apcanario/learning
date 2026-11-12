import sys, pathlib, functools, threading
site=pathlib.Path(sys.argv[1]); sys.argv=[sys.argv[0]]
sys.path.insert(0,'/home/claude/learning/kit')
import verify as V
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
class Q(SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
srv=ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Q,directory=str(site)))
threading.Thread(target=srv.serve_forever,daemon=True).start()
V.SITE=site; V.URL=f'http://127.0.0.1:{srv.server_port}/index.html'
from playwright.sync_api import sync_playwright
JS="""async (pid)=>{const p=document.getElementById(pid);const out=[];for(const f of p.querySelectorAll('figure.viz-bars')){
const sec=f.closest('.sec'); if(sec&&!sec.classList.contains('on')) p.querySelector('.seclist a[data-step="'+sec.dataset.step+'"]').click();
f.scrollIntoView({block:'center'}); await new Promise(r=>setTimeout(r,120));
const sc=f.querySelector('.viz-scroll'); const s=[...sc.querySelectorAll(':scope > svg')].find(x=>getComputedStyle(x).display!=='none');
out.push([sc.clientWidth, sc.scrollWidth, Math.round(s.getBoundingClientRect().width), s.getAttribute('width'), s.classList.contains('viz-alt')]);}return out;}"""
with sync_playwright() as p:
    br=p.chromium.launch(); ctx,pg,_=V.new_page(None,br,[],'x',320,640,True)
    for pid in ['read-a2','read-b1','r35','read-pb3']:
        try:
            pg.evaluate(f"location.hash='{pid}'"); V.ready(pg); pg.wait_for_timeout(150); print(pid, pg.evaluate(JS,pid))
        except Exception as e: print(pid,'err',str(e)[:80])
    br.close()
