import sys
from collections import deque
read = sys.stdin.readline

# init
N=int(read())
board = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(int(read())):
    x,y = map(int,read().split())
    board[x][y] = 2
moves = {}
for _ in range(int(read())):
    t,d = read().split()
    moves[int(t)] = d
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
pos = [1, 1]
dir = 1
rot = {'D':1,'L':-1}

def main():
    global pos,dir
    ERASE_LINE = '\x1b[2K'
    snake = deque([(1,1)])
    time = 0
    while True:
        time += 1
        x,y = pos
        nx = x + dx[dir]
        ny = y + dy[dir]
        if not (1<=nx<=N and 1<=ny<=N):return time
        next = board[nx][ny]
        if next == 1:return time
        else:
            board[nx][ny] = 1
            snake.append((nx,ny))
            pos = [nx,ny]
        if next != 2:
            tx,ty = snake.popleft()
            board[tx][ty] = 0
        if time in moves:
            n = moves[time]
            dir = (dir + rot[n])%4

print(main())