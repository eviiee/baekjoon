import sys
read = sys.stdin.readline

N,K = map(int,read().split())
C = [int(read()) for _ in range(N)]
C.sort(reverse=True)

r = 0
for c in C:
    r += K//c
    K %= c
print(r)