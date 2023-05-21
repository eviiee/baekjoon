import sys
read = sys.stdin.readline
from collections import deque
from itertools import product

N,M = map(int,read().split())
R = [list(map(int,read().split())) for _ in range(N)]
C = {}
A = 0
cam_type = {1:[0],2:[0,2],3:[0,1],4:[0,1,3],5:[0,1,2,3]}
cam_dir = {1:3,2:1,3:3,4:3,5:0}
dx = [-1,0,1,0]
dy = [0,1,0,-1]
cams = []
for i in range(N):
    for j in range(M):
        if R[i][j] == 0: A+=1
        elif R[i][j] != 6: cams.append([R[i][j],i,j])

def main():
    p = [0] * len(cams)
    e = [cam_dir[cam[0]] for cam in cams]
    f = True
    while f:
        if p == e : f = False
        c = 0
        sighted = [[False]*M for _ in range(N)]
        for i in range(len(cams)):
            c+=sight(cams[i]+[p[i]],sighted)
        print (c)

        t = 0
        if p[-1] == cam_dir[cams[-1][0]]:
            p[-1] = 0
            t+=1
            for i in range(len(p)-2,-1,-1):
                d = p[i] + t
                if d == cam_dir[cams[i][0]]:
                    p[i] = 0
                else :
                    p[i] += t
                    t = 0
        else : p[-1] += 1
            
def sight(cam,sighted):
    t,x,y,d = cam
    count = 0
    # if t == 5: return 0
    for dir in cam_type[t]:
        v = True
        while v:
            nx = x + dx[(d+dir)%4]
            ny = y + dy[(d+dir)%4]
            if not (0<=nx<N and 0<=ny<M) : break
            w = R[nx][ny]
            if w == 6: break
            elif not sighted[nx][ny] :
                sighted[nx][ny] = True
                x,y=nx,ny
                count+=1
    return count


main()