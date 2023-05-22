import sys
from collections import deque
read=sys.stdin.readline

N,M=map(int,read().split())
E={i:[] for i in range(1,N+1)}
K=[[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,read().split())
    E[a].append(b)
    E[b].append(a)

def bfs(s):
    q = deque([(s,0)])
    v = {s}
    K[s][s] = -1
    while q:
        n,c = q.popleft()
        for e in E[n]:
            if not e in v:
                v.add(e)
                K[s][e] = K[e][s] = c+1
                q.append((e,c+1))
    K[s][s] = 0

def main():
    v,m = 0,0
    for i in range(1,N+1):
        bfs(i)
        s = sum(K[i])/(N-1)
        if m==0 or s<m:
            v,m = i,s
    return v

print(main())
    