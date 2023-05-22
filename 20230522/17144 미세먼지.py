from collections import deque
import sys
import copy
read = sys.stdin.readline

def init():
    global R,C,T,room,dx,dy,px1,px2,py
    R,C,T = map(int,read().split())
    room = [list(map(int,read().split())) for _ in range(R)]
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    f = True
    for i in range(R):
        for j in range(C):
            if room[i][j] == -1 :
                if f:
                    px1,py = i,j
                    f = False
                else :
                    px2 = i
                    break
        else: continue
        break

def diffuse():
    global room
    tmp_room = copy.deepcopy(room)
    q = deque([])
    for i in range(R):
        for j in range(C):
            if room[i][j] >= 5: q.append((i,j))
    while q:
        x,y = q.popleft()
        d = int(room[x][y]/5)
        c = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<R and 0<=ny<C and room[nx][ny] != -1:
                tmp_room[nx][ny]+=d
                c+=1
        tmp_room[x][y] -= c*d
    room = tmp_room

def purify():
    t = deque([(px1-1,py)])
    
    d = 0
    p = px1
    for i in range(1, -2, -2):
        while t:
            x,y = t.popleft()
            while True:
                nx = x + dx[d]
                ny = y + dy[d]
                if ((p == px1 and 0<=nx<=p) or (p == px2 and p<=nx<R)) and 0<=ny<C : break
                d+=i
            if nx == p and ny == py:
                room[x][y] = 0
                break
            room[x][y] = room[nx][ny]
            t.append((nx,ny))
        d = 2
        p = px2
        t.append((px2+1,py))


init()
for _ in range(T):
    diffuse()
    purify()
print(sum([sum(row) for row in room]) + 2)