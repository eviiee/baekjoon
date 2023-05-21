from math import gcd
import sys
read=sys.stdin.readline

N=int(read())
D=[]
t=int(read())
for i in range(N-1):
    a = int(read())
    D.append(abs(t-a))
    t=a
D.sort(reverse=True)
g = D[0]
for d in D:
    g=gcd(g,d)
c = 0
for i in range(N-1):
    c+=D[i]//g-1

print(c)