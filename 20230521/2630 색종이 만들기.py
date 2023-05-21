import sys
read = sys.stdin.readline

N = int(read())
P = [list(map(int,read().split())) for _ in range(N)]
W = 0
B = 0

def d(n,r,c):
    global W,B
    if n == 1 :
        if P[r][c] == 1 : B+=1
        else : W+=1
        return
    s = sum([sum(P[i][c:c+n]) for i in range(r,r+n)])
    if s == n**2 : B+=1
    elif s == 0 : W+=1
    else :
        n//=2
        d(n,r,c)
        d(n,r,c+n)
        d(n,r+n,c)
        d(n,r+n,c+n)
    return

d(N,0,0)
print(W)
print(B)