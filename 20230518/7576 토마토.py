import sys
from collections import deque
read=sys.stdin.readline

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

M,N = map(int,read().split())
container=[list(map(int,read().split())) for _ in range(N)]

def main():

    need_riping=False

    riping = deque([])
    for r in range(N):
        for c in range(M):
            if container[r][c] == 1: riping.append((r,c,0))
            elif container[r][c] == 0: need_riping = True
    if not need_riping: return 0
    days_processed=0
    while riping:
        x,y,days = riping.popleft()
        days_processed = days
        for i in range(4):
            nx,ny = (x+dx[i],y+dy[i])
            if not (0<=nx<N and 0<=ny<M) : continue
            if container[nx][ny] == 0:
                container[nx][ny] = 1
                riping.append((nx, ny, days+1))
    for r in range(N):
        for c in range(M):
            if container[r][c] == 0 : return -1
    return days_processed


print(main())