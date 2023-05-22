import sys
read = sys.stdin.readline

N = int(read())
board = [list(map(int,read().rstrip())) for _ in range(N)]

def e(r,c,n):
    if n == 1: return str(board[r][c])
    s = sum([sum(row[c:c+n]) for row in board[r:r+n]])
    if s == n**2 : return '1'
    elif s == 0 : return '0'
    else : return '('+e(r,c,n//2)+e(r,c+n//2,n//2)+e(r+n//2,c,n//2)+e(r+n//2,c+n//2,n//2)+')'

print(e(0,0,N))