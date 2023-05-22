import sys
from math import lcm
read = sys.stdin.readline

for _ in range(int(read())):
    N,M,x,y = map(int,read().split())
    n = lcm(N,M)+x+y
    print(n)