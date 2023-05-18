# from collections import deque

# N,M = 0,0
# board = []
# visited = []
# afterbreak = []
# adj=lambda x,y:[(x+dis[0],y+dis[1]) for dis in [(-1,0),(0,1),(1,0),(0,-1)]]
# inbound=lambda x,y:True if 0<=x<N and 0<=y<M else False

# dx=[-1, 0, 1, 0]
# dy=[0, 1, 0, -1]

# def init():
#     global N,M,board,visited,afterbreak
#     data=open(0).read().rstrip().split('\n')
#     N,M=map(int,data[0].split())
#     board=list(list(map(int,list(data[i]))) for i in range(1,N+1))
#     visited=list([0]*M for _ in range(N))
#     afterbreak=list([0]*M for _ in range(N))
#     for i in range(N):
#         for j in range(M):
#             if board[i][j] == 1:
#                 visited[i][j] = -1

# def bfs(pos):

#     x,y,count,canbreak=pos
#     navigating = deque([pos])
#     visited[x][y]=afterbreak[x][y]=1

#     while navigating:
#         x,y,count,canbreak=navigating.popleft()

#         if x==N-1 and y==M-1 : return count

#         for nx,ny in adj(x,y):
#             if inbound(nx,ny):
#                 if nx==N-1 and ny==M-1 : return count+1
#                 elif canbreak:
#                     if board[nx][ny]==0 and visited[nx][ny]==0:
#                         visited[nx][ny]=afterbreak[nx][ny]=count+1
#                         navigating.append((nx,ny,count+1,True))
#                     elif board[nx][ny]==1:
#                         afterbreak[nx][ny]=count+1
#                         navigating.append((nx,ny,count+1,False))
#                 elif visited[nx][ny] == afterbreak[nx][ny] == board[nx][ny] == 0:
#                     afterbreak[nx][ny] = count+1
#                     navigating.append((nx,ny,count+1,False))
    
#     return -1
    
# def main():
#     short=bfs((0,0,1,True))
#     return short

# init()
# print(main())









#### 재풀이
from collections import deque
import sys
read=sys.stdin.readline

N,M = map(int, read().split())
board = [[int(i) for i in read().rstrip()] for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs():

    queue = deque([(0,0,0,1)])
    visited = [[[False, False]for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = True

    while queue:
        x,y,b,c=queue.popleft()
        if x==N-1 and y==M-1: return c
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (0<=nx<N and 0<=ny<M) : continue
            if board[nx][ny] == 0 and not visited[nx][ny][b]:
                visited[nx][ny][b] = True
                queue.append((nx,ny,b,c+1))
            elif board[nx][ny] == 1 and b == 0 and not visited[nx][ny][1]:
                visited[nx][ny][1] = True
                queue.append((nx,ny,1,c+1))

    return -1

print(bfs())