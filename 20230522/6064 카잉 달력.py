import sys
from math import lcm
read = sys.stdin.readline
def main():
    N,M,x,y = map(int,read().split())
    if N == x and M == y : return lcm(N,M)
    l = sorted([(N,x),(M,y)])
    a,b = l[0]
    c,d = l[1]
    for i in range(0,lcm(N,M)+1,a):
        if (i+b-1)%c+1 == d: return i+b
    else: return -1

for _ in range(int(read())):
    print(main())