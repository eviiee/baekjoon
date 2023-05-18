from collections import deque

def bsf():

    N,K = map(int,input().split())
    queue = deque([(N,0)])
    visited = {N:0}

    while queue:
        x,t = queue.popleft()
        print(x)
        if x == K: return t
        neighbors = {x-1:1,x+1:1,x*2:0}
        for neighbor in neighbors:
            nt=t+neighbors[neighbor]
            if neighbor not in visited:
                visited[neighbor]=nt
                queue.append((neighbor,nt))
            elif nt<visited[neighbor]:
                visited[neighbor]=nt
                queue.append((neighbor,nt))
            
print(bsf())