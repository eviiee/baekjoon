import sys
from collections import deque
read=sys.stdin.readline

N,M,s=map(int,read().split())
E={i:[] for i in range(1,N+1)}
for _ in range(M):
    a,b=map(int,read().split())
    E[a].append(b)
    E[b].append(a)
for i in E:
    E[i].sort()
            
def DFS(node,visited):
    print(node,end=' ')
    visited[node]=True
    for neighbor in E[node]:
        if not visited[neighbor]:
            DFS(neighbor,visited)

def main():

    newvis=lambda:{i:False for i in range(1,N+1)}

    visited=newvis()
    DFS(s,visited)

    print()

    visited=newvis()
    bfs = deque([s])
    visited[s]=True
    while bfs:
        n = bfs.popleft()
        print(n,end=' ')
        for v in E[n]:
            if not visited[v]:
                visited[v]=True
                bfs.append(v)

main()