import sys
read = sys.stdin.readline

N = int(read())
T = [list(map(int,read().split())) for _ in range(N)]

for i in range(1,N):
    for j in range(len(T[i])):
        if j == 0: T[i][j] += T[i-1][j]
        elif j == len(T[i])-1:T[i][j] += T[i-1][j-1]
        else : T[i][j] += max(T[i-1][j],T[i-1][j-1])

print(max(T[-1]))