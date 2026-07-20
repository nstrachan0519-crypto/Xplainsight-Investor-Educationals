#!/usr/bin/env python3
"""PLAINSIGHT VALIDATOR — run: python3 plainsight-validate.py [files...]
Checks every page: tag balance (stack-based), glossary resolution (every
tap-to-define term must have a definition), JS syntax (node --check),
prescription sweep (no advice language), link integrity (hrefs exist).
Part of 'check us, don't trust us': anyone can run this on the public files."""
import re, os, sys, subprocess
from html.parser import HTMLParser
VOID={'br','hr','img','input','meta','link'}
BAD=["you should buy","you should sell","we recommend","you should trade","best portfolio","you need to invest"]
class T(HTMLParser):
    def __init__(s): super().__init__(); s.st=[]; s.errs=[]
    def handle_starttag(s,t,a):
        if t not in VOID: s.st.append(t)
    def handle_endtag(s,t):
        if not s.st: s.errs.append(f"stray </{t}> L{s.getpos()[0]}")
        elif s.st[-1]==t: s.st.pop()
        else: s.errs.append(f"mismatch </{t}> L{s.getpos()[0]} vs <{s.st[-1]}>")
def check(f):
    if os.path.getsize(f) < 2000:  # S20: a truncated (0-byte) page once passed — never again
        return ["TRUNCATED? file only "+str(os.path.getsize(f))+" bytes"]
    html=open(f).read(); fails=[]
    p=T(); p.feed(html)
    if p.errs or p.st: fails.append("TAGS:"+str((p.errs+p.st)[:3]))
    scripts=re.findall(r'<script>(.*?)</script>',html,re.S)
    for i,s in enumerate(scripts):
        open('/tmp/_v.js','w').write(s)
        r=subprocess.run(["node","--check","/tmp/_v.js"],capture_output=True,text=True)
        if r.returncode!=0: fails.append("JS#%d:%s"%(i,r.stderr.splitlines()[0][:80] if r.stderr else "?"))
    alljs="".join(scripts)
    defs=set(d.lower() for d in re.findall(r'data-def="([^"$]+)"',html))
    gloss=set(k.strip().strip('"').lower() for k in re.findall(r'\n  "?([^":\n]+)"?:"',alljs))
    miss=[d for d in defs if d not in gloss]
    if miss: fails.append("GLOSSARY:"+str(miss))
    low=html.lower()
    hits=[b for b in BAD if b in low]
    if hits: fails.append("PRESCRIPTION:"+str(hits))
    for l in re.findall(r'href="(plainsight-[^"#]+)"',html):
        if not os.path.exists(l): fails.append("DEADLINK:"+l)
    return fails
files=sys.argv[1:] or sorted(f for f in os.listdir('.') if f.endswith('.html'))
bad=0
for f in files:
    fails=check(f)
    print(("FAIL " if fails else "ok   ")+f+("  "+" | ".join(fails) if fails else ""))
    bad+=bool(fails)
print(f"\n{len(files)-bad}/{len(files)} clean")
sys.exit(1 if bad else 0)
