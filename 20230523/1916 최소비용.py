from heapq import heappop,heappush
import sys
read = sys.stdin.readline

def init():
    global N,G,S,E
    N = int(read())
    M = int(read())
    G = {i:[] for i in range(1,N+1)}
    for _ in range(M):
        a,b,c = map(int,read().split())
        G[a].append((c,b))
    S,E = map(int,read().split())

def djik(a,b):
    D = [float('inf')] * (N+1)
    q = [(0,a)]
    D[a] = 0
    while q:
        d,c = heappop(q)
        if D[c] != d : continue
        if c == b : return D[c]
        for nd,nc in G[c]:
            if D[nc] > nd+d :
                D[nc] = nd+d
                heappush(q,(nd+d,nc))

def main():
    init()
    return djik(S,E)

if __name__ == '__main__':
    print(main())