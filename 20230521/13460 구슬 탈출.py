import sys
from collections import deque
read = sys.stdin.readline
N,M=map(int,read().split())
board = [list(read().rstrip()) for _ in range(N)]
r_pos = None
b_pos = None
for i in range(1,N-1):
    for j in range(1,M-1):
        if board[i][j] == 'R':
            r_pos = (i,j,'R')
            board[i][j] = '.'
        elif board[i][j] == 'B':
            b_pos = (i,j,'B')
            board[i][j] = '.'

def main():

    queue = deque([([r_pos,b_pos],0)])
    visited = set()
    visited.add((r_pos,b_pos))
    escaped = []

    td = {'left':(0,-1),'right':(0,1),'up':(-1,0),'down':(1,0)}

    while queue:

        balls, c = queue.popleft()
        if c == 10 : return -1

        for dir in td:
            if dir == 'up':
                balls.sort()
            elif dir == 'down':
                balls.sort(reverse=True)
            elif dir == 'left':
                balls.sort(key=lambda x: (x[1],x[0]))
            elif dir == 'right':
                balls.sort(key=lambda x: (x[1],x[0]),reverse=True)
            
            rp,bp = None,None

            firstball = None
            for ball in balls:
                x,y,t = ball
                while True:
                    nx = x + td[dir][0]
                    ny = y + td[dir][1]
                    w = board[nx][ny]
                    if w == 'O':
                        escaped.append(t)
                        break
                    elif w == '#' or (nx,ny) == firstball:
                        if firstball == None : firstball = (x,y)
                        if t == 'R': rp = (x,y,t)
                        else: bp = (x,y,t)
                        break
                    elif w == '.':
                        x,y=nx,ny
            if (rp,bp) in visited : continue
            elif escaped:
                if len(escaped) == 1 and escaped[0] == 'R':
                    return c+1
                else : escaped.clear()
            else:
                queue.append(([rp,bp],c+1))
                visited.add((rp,bp))

    
    else: return -1


print(main())