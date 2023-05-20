import sys
read = sys.stdin.readline

N=int(read())
H=[[0,0,0]]+[list(map(int,read().split())) for _ in range(N)]
C=[[0,0,0] for _ in range(N+1)]
C[1] = H[1]

for i in range(2,N+1):
    C[i][0] = min(C[i-1][1],C[i-1][2])+H[i][0]
    C[i][1] = min(C[i-1][0],C[i-1][2])+H[i][1]
    C[i][2] = min(C[i-1][1],C[i-1][0])+H[i][2]

print(min(C[N]))