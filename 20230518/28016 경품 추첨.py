import sys
from collections import deque
from math import gcd
read=sys.stdin.readline

N,M = map(int,read().split())
board = [list(map(int,read().split())) for _ in range(N)]

startPos = (0,board[0].index(2),1)

# def dfs(pos,checked):
    
#     print(f'checking {pos}')

#     x,y,p=pos
#     if x==N-1:
#         if checked[y]==0:checked[y]=[1,p]
#         else:
#             p__=checked[y][0]
#             __p=checked[y][1]
#             denom=__p*p
#             numer=__p+(p__*p)
#             _gcd=gcd(denom,numer)
#             denom//=_gcd
#             numer//=_gcd
#             checked[y]=[numer,denom]
#         return
#     for div in divs(x,y):
#         nx,ny,nb=div
#         dfs((nx,ny,nb*p),checked)

def divs(x,y):
    divs = []
    can_go_left=can_go_right=False

    if board[x+1][y] == 0:
        divs.append((x+1,y,1))
        return divs
    
    if  0<y and board[x+1][y-1] == 0 and board[x][y-1] ==0 : can_go_left=True
    if  y<M-1 and board[x+1][y+1] == 0 and board[x][y+1] ==0 : can_go_right=True

    branch = 0
    # DFS 쓸떄.
    # if can_go_right or can_go_left: branch=2
    # elif can_go_left + can_go_right == 0: return divs
    # else : branch = 1
    if can_go_right != can_go_left: branch=2
    elif can_go_left + can_go_right == 0: return divs
    else : branch = 1

    if can_go_left : divs.append((x+1,y-1,branch))
    if can_go_right : divs.append((x+1,y+1,branch))
    return divs

def bfs(startPos,results):
    falling = deque([startPos])
    

def main():
    
    results=[0]*M

    # dfs(startPos,results)
    p,n=0,-1
    for i in range(M):
        if results[i]!=0:
            temp=results[i][0]/results[i][1]
            if temp>p:
                n=i
                p=temp

    print(n)

main()