from collections import deque
import sys
read=sys.stdin.readline

N,M,F = map(int, read().split())
maps = [list(map(int,read().split())) for _ in range(N)]
s_x, s_y = map(int,read().split())
cs = {}
for _ in range(M):
    i,j,k,l = map(int,read().split())
    cs[(i-1,j-1)] = tuple((k-1,l-1))

for cx,cy in cs.keys():
    maps[cx][cy] = 2

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(pos):

    global N,M,F,maps
    x,y,s = pos
    visited = []
    visited = resetV(visited,x,y)
    queue = deque([])
    resetQ(queue,x,y,s)

    while queue:
        x,y,s,c = queue.popleft()
        print(f'{x},{y} - customer {s} remaining fuels {F}')
        if c > F : return -1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                w = maps[nx][ny]
                if w == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny,s,c+1))
                elif not s and w == 2:
                    visited = resetV(visited,nx,ny)
                    resetQ(queue,nx,ny,True)
                    maps[nx][ny] = 0
                    gx,gy = cs[tuple((nx,ny))]
                    maps[gx][gy] = 3
                    F-=c+1
                    print(f'found cumstoer after {c+1} moves at {nx},{ny}')
                elif s and w == 3:
                    F+=c+1
                    visited = resetV(visited,nx,ny)
                    resetQ(queue,nx,ny,False)
                    maps[nx][ny] = 0
                    M-=1
                    if M==0:return F
                    print(f'reached destination after {c+1} moves at {nx},{ny}')

    print('what???',M)
                    
def resetV(v,x,y):
    global N
    v = [[False for _ in range(N)] for _ in range(N)]
    v [x][y] = True
    return v

def resetQ(q,x,y,s):
    q.clear()
    q.append((x,y,s,0))

def main():
    print(bfs((s_x-1,s_y-1,False)))

main()