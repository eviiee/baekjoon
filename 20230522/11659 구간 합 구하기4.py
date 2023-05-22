import sys
read = sys.stdin.readline

N,M = map(int,read().split())
D = [0]+list(map(int,read().split()))

for i in range(1,N+1): D[i] += D[i-1]

for _ in range(M) :
    a,b = map(int,read().split())
    print(D[b] - D[a-1])