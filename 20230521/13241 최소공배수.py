import sys

# math의 lcm 이용 (least common multiple, 최소공배수)
from math import lcm
def lcm_method():
    a,b=map(int,sys.stdin.readline().split())
    print(lcm(a,b))

# 유클리드 호제법 이용
def gcd(a,b):
    r = a%b
    if r==0: return b
    return gcd(b,r)

def euclidean_method():
    a,b = map(int,sys.stdin.readline().split())
    a,b = max(a,b),min(a,b)
    print(a*b//gcd(a,b))

# 실행
euclidean_method()