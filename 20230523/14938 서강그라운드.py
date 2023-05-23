import sys
from heapq import heappop,heappush
read = sys.stdin.readline

def init():
    global N,M,D,I,G
    N,M,R = map(int,read().split())
    I = [0] + list(map(int,read().split()))
    G = {i:[] for i in range(1,N+1)}
    for _ in range(R):
        a,b,c = map(int,read().split())
        G[a].append((c,b))
        G[b].append((c,a))
    D = [[float('inf')] * (N+1) for _ in range(N+1)]
        
def d(s):
    q = [(0,s)]
    D[s][s] = 0

    while q:
        d,c = heappop(q)
        if D[s][c] != d: continue
        for nd,nc in G[c]:
            if nd+d < D[s][nc]:
                D[s][nc] = nd+d
                heappush(q,(nd+d,nc))
    
    c = 0
    for i in range(1,N+1):
        if D[s][i] <= M: c+=I[i]
    
    return c

def main():
    init()
    m = 0
    for i in range(1,N+1):
        m = max(m,d(i))
    return m

if __name__ == '__main__':
    print(main())