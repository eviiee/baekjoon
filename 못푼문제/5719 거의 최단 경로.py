from heapq import heappop, heappush
from collections import deque
import sys
read = sys.stdin.readline

def init():
    global G,s,e,N
    N,M = map(int,read().split())
    if N==M==0 : return True
    s,e = map(int,read().split())
    G = {i:set() for i in range(N)}
    for _ in range(M):
        a,b,c = map(int,read().split())
        G[a].add((c,b))

def dj(s,e):
    D = [float('inf')]*N
    q = [(0,s)]
    D[s] = 0
    while q:
        d,c = heappop(q)
        if D[c] != d : continue
        if c == e : return D[e]
        for nd,nc in G[c]:
            if nd+d < D[nc]:
                D[nc] = nd+d
                heappush(q,(nd+d,nc))
    else : return -1

def bfs(s,e,sd):
    q = deque([(s,0)])
    V = [float('inf')]*N
    H = [[]]*N
    while q:
        c,d = q.popleft()
        if d>V[c] : continue
        for nd,nc in G[c]:
            if nd + d > sd : continue
            if nd + d <= V[nc] :
                


def main():
    while True:
        if init(): break
        sd = dj(s,e,first=True)
        print(r)

if __name__ == '__main__':
    main()