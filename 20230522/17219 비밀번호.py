import sys
read = sys.stdin.readline

N,M = map(int,read().split())
d = {s:p for s,p in [read().split() for _ in range(N)]}
for _ in range(M):print(d[read().rstrip()])