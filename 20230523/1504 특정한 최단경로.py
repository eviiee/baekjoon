import sys
from heapq import heappop as pop, heappush as push
read = sys.stdin.readline

def init():
    global N,E,G
    N,E = map(int,read().split())
    G = {i:[] for i in range(1,N+1)}
    for _ in range(E):
        a,b,c = map(int,read().split())
        G[a].append((c,b))
        G[b].append((c,a))

def main():
    init()
    w1,w2 = map(int,read().split())
    W1 = [1,w1,w2,N]
    W2 = [1,w2,w1,N]
    d1=0
    d2=0
    for i in range(3):
        dt = d(W1[i],W1[i+1])
        if dt != -1 : d1+=dt
        else :
            d1 = -1
            break
    for i in range(3):
        dt = d(W2[i],W2[i+1])
        if dt != -1 : d2+=dt
        else :
            d2 = -1
            break
    return min(d1,d2)

def d(a,b):
    I = float('inf')
    D = [I for _ in range(N+1)]
    D[a] = 0
    E = [(0,a)]
    while E:
        d,c = pop(E)
        if not D[c] == d : continue
        if c == b : return D[c]
        for nd,nc in G[c]:
            if nd+d < D[nc]:
                D[nc] = nd+d
                push(E,(nd+d,nc))
    else: return -1

if __name__ == '__main__':
    print(main())