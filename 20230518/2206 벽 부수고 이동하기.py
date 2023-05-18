import sys
from collections import deque
from copy import deepcopy
# read=sys.stdin.readline

N,M = 0,0
original_board = []
walls = set()
adj=lambda x,y:[(x+dis[0],y+dis[1]) for dis in [(-1,0),(0,1),(1,0),(0,-1)]]
inbound=lambda x,y:True if 0<=x<N and 0<=y<N else False

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def init():
    global N,M,original_board
    data=open(0).read().rstrip().split('\n')
    N,M=map(int,data[0].split())
    original_board=list(list(map(int,list(data[i]))) for i in range(1,N+1))
    for i in range(N):
        for j in range(M):
            if original_board[i][j] == 1:
                walls.add((i,j))

def bfs(board, pos):

    x,y,count=pos
    navigating = deque([pos])
    board[x][y]=1

    while navigating:
        x,y,count=navigating.popleft()
        if x==N-1 and y==M-1:
            return count
        for nx,ny in adj(x,y):
            if inbound(nx,ny) and board[nx][ny] == 0:
                navigating.append((nx,ny,count+1))
                board[nx][ny] = 1

    return -1

def main():
    shortest=-1
    # 벽을 부수지 않은 최단경로
    board = deepcopy(original_board)
    normalcount = bfs(board,(0,0,1))
    # 벽을 부셨을 경우 최단경로

    return shortest
    
init()
print(main())