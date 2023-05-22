import sys
from heapq import heappop, heappush
read = sys.stdin.readline

for _ in range(int(read())):
    key = 0
    a = []
    b = []
    d = set()
    for _ in range(int(read())):
        t,n = read().split()
        n = int(n)
        if t == 'I':
            heappush(a,(n,key))
            heappush(b,(-n,key))
        elif t == 'D':
            l = a if n == -1 else b
            while True and l:
                _,k = heappop(l)
                if k not in d:
                    d.add(k)
                    break
        key+=1
    min = max = None
    while a:
        n, key = heappop(a)
        if key not in d:
            min = n
            break
    else:
        print ('EMPTY')
        continue
    while b:
        n, key = heappop(b)
        if key not in d:
            max = -n
            break
    print(f'{max} {min}')