import sys
from collections import deque
read=sys.stdin.readline

t=int(read())
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]




def main():

    def bfs(land,pos):
        
        withinarea = deque([pos])
        
        while withinarea:
            x,y=withinarea.popleft()
            adjs = [(x+dx[i],y+dy[i]) for i in range(4)]
            for nx,ny in adjs:
                if 0<=nx<N and 0<=ny<M and land[nx][ny] == 1:
                    land[nx][ny]=0
                    withinarea.append((nx,ny))

                    
    M,N,K=map(int,read().rstrip().split())
    land=[[0]*M for _ in range(N)]

    for _ in range(K):
        b,a=map(int,read().rstrip().split())
        land[a][b]=1

    count=0
    for r in range(N):
        for c in range(M):
            if land[r][c] != 0:
                land[r][c] = 0
                count+=1
                bfs(land,(r,c))
    print(count)



for _ in range(t): main()