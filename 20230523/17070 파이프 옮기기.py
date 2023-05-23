import sys
read = sys.stdin.readline

N = int(read())
R = [[0]*(N+1)]
for _ in range(N):
    R.append([0]+list(map(int,read().split())))
D = [[[0]*(N+1) for _ in range(N+1)] for _ in range(3)]

# 0 : 가로 1 : 대각 2: 세로
D[0][1][2] = 1
for i in range(1,N+1):
    for j in range(2,N+1):
        if R[i][j] == 0:
            D[0][i][j] += D[1][i][j-1] + D[0][i][j-1]
            D[2][i][j] += D[1][i-1][j] + D[2][i-1][j]
        if R[i][j] == R[i-1][j] == R[i][j-1] == 0:
            D[1][i][j] += sum([D[k][i-1][j-1] for k in range(3)])
print(sum([D[i][-1][-1] for i in range(3)]))