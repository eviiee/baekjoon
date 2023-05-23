from heapq import heappop,heappush
import sys
read = sys.stdin.readline

def init():
    global G,V,S
    V,e = map(int,read().split())
    S = int(read())
    G = {i:[] for i in range(1,V+1)}
    for _ in range(e):
        a,b,c = map(int,read().split())
        G[a].append((c,b))

def djik():
    D = [float('inf')]*(V+1)
    q = [(0,S)]
    D[S] = 0

    while q:
        d,v = heappop(q)
        if D[v] != d : continue
        for nd,nv in G[v]:
            if D[nv] > nd + d:
                D[nv] = nd+d
                heappush(q,(nd+d,nv))
    
    return D[1:]

def main():
    init()
    D = djik()
    for d in D:
        print(d if d!=float('inf') else 'INF')

if __name__ == '__main__':
    main()