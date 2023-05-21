from math import lcm
input()
N=sorted(list(map(int,input().split())))
l=N[0]*N[-1]
for n in N: l = lcm(n,l)
print(l)