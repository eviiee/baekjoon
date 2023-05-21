from math import gcd
ax,ay=map(int,input().split())
bx,by=map(int,input().split())
x,y = ax*by+ay*bx,ay*by
d=gcd(x,y)
x//=d
y//=d
print(f'{x} {y}')