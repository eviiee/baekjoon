from collections import deque
import sys
read=sys.stdin.readline

N,M = map(int, read().split())
maps = [list(read().rstrip()) for _ in range(N)]
waters=[]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for i in range(N):
    for j in range(M):
        if maps[i][j] == 'S':s=(i,j,True,0)
        elif maps[i][j] == '*':waters.append((i,j,False,0))

def bfs():
    visited = [[False for _ in range(M)] for _ in range(N)]
    for x,y,h,t in waters: visited[x][y] = True
    visited[s[0]][s[1]] = True
    queue = deque([])
    queue.extend(waters)
    queue.append(s)

    while queue:
        x,y,h,t = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if not h:
                    if maps[nx][ny] in {'S','.'}:
                        maps[nx][ny] = '*'
                        queue.append((nx,ny,h,t+1))
                if h:
                    if maps[nx][ny] == 'D': return t+1
                    elif maps[nx][ny] == '.' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        maps[nx][ny] = 'S'
                        maps[x][y] = '.'
                        queue.append((nx,ny,h,t+1))
    return ('KAKTUS')

print(bfs())