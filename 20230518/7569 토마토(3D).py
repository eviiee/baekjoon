import sys
from collections import deque
read=sys.stdin.readline

dx=[-1, 0, 1, 0, 0, 0]
dy=[0, 1, 0, -1, 0, 0]
dh=[0, 0, 0, 0, 1, -1]

M,N,H = map(int,read().split())
container=list(list(list(map(int,read().strip().split())) for _ in range(N)) for _ in range(H))

def main():

    need_riping=False

    riping = deque([])
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if container[h][r][c] == 1: riping.append((h,r,c,0))
                elif container[h][r][c] == 0: need_riping = True
    if not need_riping: return 0
    days_processed=0
    while riping:
        h,x,y,days = riping.popleft()
        days_processed = days
        for i in range(6):
            nh,nx,ny = (h+dh[i]),x+dx[i],y+dy[i]
            if not (0<=nx<N and 0<=ny<M and 0<=nh<H) : continue
            if container[nh][nx][ny] == 0:
                container[nh][nx][ny] = 1
                riping.append((nh, nx, ny, days+1))
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if container[h][r][c] == 0 : return -1
    return days_processed


print(main())