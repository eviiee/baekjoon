import sys
read = sys.stdin.readline
from collections import deque

N,M = map(int,read().split())
l = {a:b for a,b in [map(int,read().split()) for _ in range(N+M)]}
v = [0] * 101

q = deque([1])

while q:
    x = q.popleft()
    for i in range(1,7):
        n = x+i
        if 1<=n<=100 and v[n] == 0:
            v[n] = v[x]+1
            if n in l and v[l[n]] == 0:
                v[l[n]] = v[x] + 1
                q.append(l[n])
            elif n not in l: q.append(n)

print(v[100])