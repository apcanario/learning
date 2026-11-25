import sys,re,subprocess
row=sys.argv[1]; src=sys.argv[2] if len(sys.argv)>2 else None
s=open(src).read() if src else subprocess.run(['python3','kit/next_prompt.py','--row',row],capture_output=True,text=True).stdout
open(f'/tmp/rules/{row}-prompt.txt','w').write(s)
def cut(a,b):
    i=s.index(a); j=s.index(b,i); return s[i:j].strip()
w=cut('- The writer rules of this course','**4. The fresh check.**')
fl=cut('Open flags that name this unit:','**Quality-review rule**') if 'Open flags that name this unit:' in s else ''
open(f'/tmp/rules/{row}-writer.txt','w').write(w+'\n\n'+fl+'\n')
c=cut('Beyond the skill\'s items it runs the seven passes','Before any fix,')
open(f'/tmp/rules/{row}-checker.txt','w').write(c+'\n')
print(row,len(s),len(w),len(fl),len(c)); print(fl[-400:])
