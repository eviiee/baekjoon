import sys
from collections import deque
read = sys.stdin.readline

def main():
    N,M = map(int,read().split())
    P = [[False]*(M+1) for _ in range(N+1)]
    T = list(map(int,read().split()))[1:]
    for i in range(1,M+1):
        p = list(map(int,read().split()))[1:]
        for j in p: P[j][i] = True
    
    q = deque([])
    vp = [False] * (M+1)
    vt = [False] * (N+1)
    for i in range(1,M+1):
        for t in T:
            if P[t][i] and not vp[i] :
                vp[i] = True
                q.append(i)
    
    while q:
        party = q.popleft()
        for i in range(1,N+1):
            if P[i][party] and not vt[i]:
                vt[i] = True
                for j in range(1,M+1):
                    if P[i][j] and not vp[j]:
                        q.append(j)
                        vp[j] = True
    
    return vp.count(False)-1


print(main())