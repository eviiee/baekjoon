import sys
read = sys.stdin.readline
for _ in range(int(read())):
    N = int(read())
    count = [[0 for _ in range(2)] for _ in range (N+1)]
    count[0][0] = 1
    if N>0:count[1][1] = 1
    if N>1:
        for i in range(2,N+1):
            count[i][0] = count[i-1][0] + count[i-2][0]
            count[i][1] = count[i-1][1] + count[i-2][1]
    print(f'{count[N][0]} {count[N][1]}')