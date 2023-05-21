import sys
import copy
read=sys.stdin.readline

N,M = map(int,read().split())

board = [list(map(int,read().split())) for _ in range(N)]
P = [[0]*M for _ in range(N)]
need_check = set()
for i in range(M):
    if board[0][i] == 2:
        need_check.add(i)
        P[0][i] = 1

for i in range(1,N):
    if len(need_check) == 0 :
        print(-1)
        break
    for j in copy.copy(need_check):
        w = board[i][j]
        p = P[i-1][j]
        if w == 0:
            P[i][j] += p
        elif w == 1:
            need_check.remove(j)
            if board[i-1][j-1] == board[i][j-1] == 0:
                need_check.add(j-1)
                P[i][j-1] += p//2
            if board[i-1][j+1] == board[i][j+1] == 0:
                need_check.add(j+1)
                P[i][j+1] += p//2
else:
    r = 10000
    for i in range(M):
        if 0 < P[-1][i] < r : r = i
    print(r)