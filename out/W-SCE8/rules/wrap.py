"""wrap.py BUILD_INDEX OUT: put the build's shell inside the wrapper the live page carries (prefix and suffix taken from the saved live shell)."""
import sys
live=open('/tmp/pub/live-index.html',encoding='utf-8').read()
start=open('/tmp/pub/start-build/index.html',encoding='utf-8').read()
i=live.find(start); assert i>=0
pre,suf=live[:i],live[i+len(start):]
open(sys.argv[2],'w',encoding='utf-8').write(pre+open(sys.argv[1],encoding='utf-8').read()+suf)
print('wrapped',len(pre),len(suf))
