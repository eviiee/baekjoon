import sys
read = sys.stdin.readline

n,k = map(int,read().split())

v = [0 for _ in range(k+1)]
cs = set(int(read()) for _ in range(n))
v[0] = 1

for c in cs:
    for i in range(k-c+1):
        v[i+c] += v[i]

print(v[-1])