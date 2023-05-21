from collections import deque
N,K = map(int,input().split())

def bfs():
    if N==K: return 0
    V = [False for _ in range(100001)]
    searching = deque([(N,0)])
    V[N] = True
    while searching:
        n,c = searching.popleft()
        for nn in (n-1,n+1,2*n):
            if 0<=nn<=100000 and not V[nn]:
                if nn == K:
                    return c+1
                V[nn] = True
                searching.append((nn,c+1))

print(bfs())