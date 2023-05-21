import sys
read=sys.stdin.readline

P=[True for _ in range(1000001)]
P[:3]=[False,False,True]
p={2}
for i in range(4,len(P),2):
    P[i] = False
for i in range(3,len(P),2):
    if P[i]:
        for j in range(i**2,len(P),i):
            P[j]=False
        p.add(i)
s = sorted(p)
for _ in range(int(read())):
    n=int(read())
    c=0
    for x in s:
        if x*2 > n: break
        if n-x in p: c+=1
    print(c)