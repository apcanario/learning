import sys, pathlib, functools, threading
sys.argv=[sys.argv[0]]
sys.path.insert(0,'/home/claude/learning/kit')
import verify as V
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
class Q(SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
site=pathlib.Path('/tmp/academy-before')
srv=ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Q,directory=str(site)))
threading.Thread(target=srv.serve_forever,daemon=True).start()
V.SITE=site; V.URL=f'http://127.0.0.1:{srv.server_port}/index.html'
from playwright.sync_api import sync_playwright
fails=[]
with sync_playwright() as p:
    br=p.chromium.launch(); V.check_phone_figures(br,fails); br.close()
import collections
print(len(fails)); print(collections.Counter(f.split(': ')[1].split(' (')[0][:40] for f in fails))
for f in fails[:6]: print(f)
