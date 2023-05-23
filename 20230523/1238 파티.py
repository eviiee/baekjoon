import sys
import heapq
read = sys.stdin.readline

def init():
    global N,M,X,G
    N,M,X = map(int,read().split())
    G = {i:[] for i in range(N+1)}
    for _ in range(M):
        a,b,c = map(int,read().split())
        G[a].append((c,b))

def djik(sc):
    BV = [-1]*(N+1)
    BV[sc] = 0
    dj = []
    heapq.heappush(dj,(0,sc))
    while dj:
        d,c = heapq.heappop(dj)
        if BV[c] != d : continue
        for nd,nc in G[c]:
            if BV[nc] == -1 or BV[nc] > nd + d:
                BV[nc] = nd + d
                heapq.heappush(dj,(nd+d,nc))
    
    return BV

def main():
    init()
    D = djik(X)
    for c in range(1,N+1):
        D[c] += djik(c)[X]
    return max(D)

print(main())