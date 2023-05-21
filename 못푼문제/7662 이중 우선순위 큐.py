import sys
from heapq import heappop as D, heappush as I
read = sys.stdin.readline
for _ in range(int(read())):
    q = []
    for _ in range(int(read())):
        a,b = read().split()
        b=int(b)
        if a == 'D' and q:
            if b == 1:
                q.sort()
                q.pop()
            elif b == -1:
                D(q)
        elif a == 'I':
            I(q,b)
    q.sort()
    print(f'{q[-1]} {q[0]}' if q else 'EMPTY')