import sys
from collections import deque
read=sys.stdin.readline

n,m=int(read()),int(read())
pcs={i:[] for i in range (1,n+1)}

for _ in range(m):
    a,b=map(int,read().split())
    pcs[a].append(b)
    pcs[b].append(a)

def bfs():

    visited={i:False for i in range(1,n+1)}
    visited[1] = True
    searching=deque([1])
    count=0
    while searching:
        pc = searching.popleft()
        for next in pcs[pc]:
            if not visited[next]:
                count+=1
                visited[next]=True
                searching.append(next)
        
    print(count)

bfs()