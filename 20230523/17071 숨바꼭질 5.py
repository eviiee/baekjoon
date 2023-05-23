from collections import deque

def init():
    global D,N,K
    N,K = map(int,input().split())
    D = {K:0}
    i = 1
    t = K
    while True:
        t += i
        if t>500000 : break
        else :
            D[t] = i
            i += 1

def bfs():
    if N == K : return 0
    q = deque([(N,0)])
    V = [[False] * 500001 for _ in range(2)] 
    V[0][N] = True
    m = len(D)
    s = float('inf')
    while q:
        n,t = q.popleft()
        if t == m or t >= s: break
        for i in [n*2,n-1,n+1]:
            if i<0 or i>500000: continue
            if i in D and t + 1 <= D[i]:
                if (D[i] - t - 1)%2 == 0:
                    s = min(s,D[i])
            if not V[(t+1)%2][i]:
                V[(t+1)%2][i] = True
                q.append((i,t+1))
    return s if s != float('inf') else -1

def main():
    init()
    return bfs()

if __name__ == '__main__':
    print(main())