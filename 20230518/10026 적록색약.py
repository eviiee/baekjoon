from collections import deque
from copy import deepcopy as d
import sys
read=sys.stdin.readline

N=int(read())
board1=[list(read().strip()) for _ in range(N)]
board2=d(board1)
adj=lambda x,y:[(x+dis[0],y+dis[1]) for dis in [(-1,0),(0,1),(1,0),(0,-1)]]
inbound=lambda x,y:True if 0<=x<N and 0<=y<N else False
first_compute=True

def bfs(board, first_x, first_y):

    global first_compute
    val=board[first_x][first_y]

    issame={'R':False, 'G':False, 'B':False}
    issame[val]=True

    if not first_compute and (issame['R'] or issame['G']):
        issame['R']=issame['G']=True
    
    search_area = deque([(first_x,first_y)])
    board[first_x][first_y]=0

    while search_area:
        x,y=search_area.popleft()
        for nx,ny in adj(x,y):
            if inbound(nx,ny) and issame.get(board[nx][ny],False):
                board[nx][ny]=0
                search_area.append((nx,ny))

for _ in range(2):
    board = board1 if first_compute else board2

    count=0
    for r in range(N):
        for c in range(N):
            if board[r][c]!=0:
                bfs(board,r,c)
                count+=1

    print(count)
    first_compute = False

