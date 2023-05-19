from collections import deque
import sys
read=sys.stdin.readline

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def init():
    global N,M,F,maps,pos,passengers

    N,M,F = map(int,read().split())
    maps = [[0] * (N+1)]
    for _ in range(N) : maps.append([0]+list(map(int,read().split())))
    pos = list(map(int,read().split()))
    passengers={}
    for _ in range(M):
        i,j,k,l = map(int,read().split())
        passengers[(i,j)] = (k,l)
        maps[i][j] = 2

def bfs(with_passenger):
    global N,F,maps,pos,passengers

    visited = [[0]*(N+1) for _ in range(N+1)]
    queue = deque([])
    init_x,init_y = pos

    if not with_passenger and maps[init_x][init_y] == 2:
        maps[init_x][init_y] = 0
        return 0
    elif with_passenger : destination = passengers[(init_x,init_y)]
    
    queue.append((init_x,init_y,0))

    ps = []
    count = 0
    while queue:
        x,y,c = queue.popleft()
        if len(ps) > 0 and c >= count : break
        ### 연료 모자라면 return -1
        if c >= F : return -1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not (1<=nx<=N and 1<=ny<=N) : continue
            w = maps[nx][ny]
            ## 승객을 태우고 destination을 만난 경우
            if with_passenger and (nx,ny) == destination:
                pos = [nx,ny]
                return c+1
            ## 승객 없이 손님을 만난 경우
            elif not with_passenger and w == 2:
                ps.append([nx,ny])
                visited[nx][ny] = 1
                count = c+1
            ## 아직 방문하지 않은 좌표일 경우
            elif w != 1 and visited[nx][ny] == 0 and len(ps) == 0:
                visited[nx][ny] = 1
                queue.append((nx,ny,c+1))
            
    if len(ps) > 0:
        ps.sort()
        px,py = ps[0]
        maps[px][py] = 0
        pos = [px,py]
        return count
    else: return -1


def main():
    global M,F
    init()

    # 지도에 승객의 수만큼 [태우고, 내리기]를 반복
    for _ in range(M):
        to_passenger = bfs(False)
        if to_passenger == -1 : return -1
        F -= to_passenger

        to_destination = bfs(True)
        if to_destination == -1 : return -1
        F += to_destination

    return F

print(main())