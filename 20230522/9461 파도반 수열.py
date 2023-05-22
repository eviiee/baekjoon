import sys
read = sys.stdin.readline
D = [0]*101
D[:6] = [0,1,1,1,2,2]
for i in range(6,101): D[i] = D[i-1] + D[i-5]
for _ in range(int(read())):
    print(D[int(read())])