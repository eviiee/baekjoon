from random import randint as r

n,m=6,4

print(f'{n} {m}')
for i in range(n):
    for j in range(m):
        print(r(0,1) if not ((i == 0 and j == 0) or (i == n-1 and j == m-1)) else 0,end='')
    print()
