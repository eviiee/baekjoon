import sys
from collections import deque
read = sys.stdin.readline

N,M=map(int,read().split())
V = [False] * (N+1)
E = {i:[] for i in range(1,N+1)}

for _ in range(M):
    a,b = map(int,read().split())
    E[a].append(b)
    E[b].append(a)

def bfs(r):
    
    q = deque([r])

    while q:
        v = q.popleft()
        for e in E[v]:
            if not V[e]:
                V[e] = True
                q.append(e)
    
    return 1

def main():
    c = 0
    for i in range(1,N+1):
        if not V[i]: c+=bfs(i)
    print(c)

main()