import sys
read = sys.stdin.readline

N = int(read())
P = [list(map(int,read().split())) for _ in range(N)]
C = {i:0 for i in range(-1,2)}

def ct(r,c,n):
    if n == 1 :
        C[P[r][c]]+=1
        return
    s = [0,0,0]
    for x in range(r,r+n):
        for y in range(c,c+n):
            s[P[x][y]+1]+=1
    if s[2] == n**2 : C[1]+=1
    elif s[0] == n**2 : C[-1]+=1
    elif s[1] == n**2 : C[0]+=1
    else:
        d = n//3
        for i in range(3):
            for j in range(3):
                ct(r+(i*d),c+(j*d),d)

ct(0,0,N)
print(*C.values(),sep='\n')