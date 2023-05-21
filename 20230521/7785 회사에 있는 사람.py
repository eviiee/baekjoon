import sys
read=sys.stdin.readline
write=sys.stdout.write
E=set()
for _ in range(int(read())):
    n,s=read().split()
    if s=='enter':E.add(n)
    else: E.remove(n)
E=sorted(list(E),reverse=True)
for e in E:write(e+'\n')