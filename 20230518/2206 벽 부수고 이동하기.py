from collections import deque

N,M = 0,0
board = []
walls = []
adj=lambda x,y:[(x+dis[0],y+dis[1]) for dis in [(-1,0),(0,1),(1,0),(0,-1)]]
inbound=lambda x,y:True if 0<=x<N and 0<=y<M else False

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def init():
    global N,M,board
    data=open(0).read().rstrip().split('\n')
    N,M=map(int,data[0].split())
    board=list(list(map(int,list(data[i]))) for i in range(1,N+1))
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                board[i][j] = -1
                walls.append((i,j))
                print(i,j)
    print(board)
    print(walls)

def bfs(board, pos, checkforwalls=False):

    x,y,count=pos
    navigating = deque([pos])
    board[x][y]=1 if not checkforwalls else board[x][y]

    while navigating:
        x,y,count=navigating.popleft()
        if x==N-1 and y==M-1:
            return count
        for nx,ny in adj(x,y):
            if inbound(nx,ny):
                if (board[nx][ny] == 0 or (checkforwalls and board[nx][ny] > board[x][y])):
                    navigating.append((nx,ny,count+1))
                    board[nx][ny] = count+1

    return -1

def main():

    # 벽을 부수지 않은 최단경로
    bfs(board,(0,0,1))
    # 벽을 부셨을 경우 최단경로

    broken_walls = deque([])
    broken_walls.extend(walls)

    while broken_walls:
        wall_x,wall_y=broken_walls.popleft()
        board[wall_x][wall_y]=999999999
        for nx,ny in adj(wall_x,wall_y):
            if inbound(nx,ny) and board[nx][ny] != -1 and board[nx][ny] != 0:
                bfs(board, (nx,ny,board[nx][ny]),checkforwalls=True)
        board[wall_x][wall_y]=-1
    print(board)
    return board[N-1][M-1] if board[N-1][M-1]!=0 else -1
    
init()
print(main())