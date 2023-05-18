import sys
from collections import deque
read=sys.stdin.readline

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

n,m=map(int,read().split())
maze=[list(map(int,list(read().strip()))) for _ in range(n)]

def bfs():

    searching=deque([(0,0,1)])

    while searching:
        cur_x,cur_y,c = searching.popleft()
        if cur_x==n-1 and cur_y==m-1:
            print(c)
            searching.clear()
            break
        adjs = [(cur_x+dx[i],cur_y+dy[i]) for i in range(4)]
        for x,y in adjs:
            if 0<=x<n and 0<=y<m and maze[x][y]!=0:
                maze[x][y]=0
                searching.append((x,y,c+1))

bfs()