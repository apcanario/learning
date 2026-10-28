import re,html,pathlib,sys
R=pathlib.Path('/tmp/claude-0/-home-claude/375fb532-42ed-5373-819b-35a5b714eedb/scratchpad/kit/personal-mythology')
def words(c,i):
    s=(R/c/f'r-{i}.html').read_text().split('<h2>Self-test</h2>')[0]
    t=html.unescape(re.sub(r'<[^>]+>',' ',s)).lower()
    return re.findall(r"[a-z0-9']+",t)
def sh(w,n=7): return {' '.join(w[k:k+n]) for k in range(len(w)-n+1)}
def names(c,i):
    s=(R/c/f'r-{i}.html').read_text().split('<h2>Self-test</h2>')[0]
    t=html.unescape(re.sub(r'<[^>]+>',' ',s))
    return set(re.findall(r'\b[A-Z][a-z]{3,}\b',t))
STOP={'The','This','That','There','These','Those','When','What','Where','Which','While','With','From','Their','They','Then','Both','After','Before','Rome','Roman','Romans','Greek','Greeks','Senate','Italy','Also','Only','Most','Some','Each','Even','Here','Such','Later','Early','First','Second','Third','Under','Over','Between','Against','Because','Modern','Ancient','Book','Books','Where','Module','Republic','Empire','Latin','About','Into','Within','Without','Since','Thus','Though','Although','Many','More','Nothing','Every','Another','Other','Whether','Would','Could','Should','Being','Among','Those','Across','Year','Years','Century'}
def pair(a,b):
    (ca,ia),(cb,ib)=a,b
    wa,wb=words(ca,ia),words(cb,ib); A,B=sh(wa),sh(wb)
    common=A&B
    # rough share of later module built on shared shingles: words covered
    cov=len(common)/max(1,len(B))
    na,nb=names(ca,ia)-STOP,names(cb,ib)-STOP
    j=len(na&nb)/max(1,len(na|nb))
    return len(wa),len(wb),len(common),cov,j,sorted(na&nb)[:40]
pairs=[l.split() for l in sys.stdin if l.strip()]
for p in pairs:
    a=('rome' if not p[0].startswith('g') else 'greece', p[0].lstrip('g')); b=('rome' if not p[1].startswith('g') else 'greece', p[1].lstrip('g'))
    la,lb,c,cov,j,nm=pair(a,b)
    print(f'{p[0]:>6} -> {p[1]:<6} words {la:>5}/{lb:<5} shared 7-shingles {c:>3} ({cov*100:4.1f}% of later)  name-Jaccard {j:.2f}')
