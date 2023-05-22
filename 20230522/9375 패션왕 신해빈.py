import sys
read = sys.stdin.readline

for _ in range(int(read())):
    d = {}
    for _ in range(int(read())):
        n,t = read().split()
        if t not in d: d[t] = 2
        else : d[t] += 1
    d = list(d.values())
    c = 1
    for i in d:c*=i
    print(c-1)