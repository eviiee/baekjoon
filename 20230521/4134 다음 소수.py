import sys
from math import sqrt,floor
read=sys.stdin.readline

def p(n):
    if n<=2: return 2
    for i in range(n,2*n):
        for j in range(2,floor(sqrt(i))+1):
            if i%j == 0:break
        else: return i

for _ in range(int(read())):
    print(p(int(read())))