import sys
read = sys.stdin.readline

K,N = map(int,read().rstrip().split())
l = [int(read()) for _ in range(K)]
l.sort()
r = {}

x = l[0]*K//N
y = l[-1]*K//N+1
while x<y:
    m = (x+y)//2
    c = sum([p//m for p in l])
    if c >= N : x = m + 1
    elif c < N : y = m

print (m)