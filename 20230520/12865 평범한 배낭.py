import sys
read = sys.stdin.readline
N,K = map(int,read().split())
bag = [0 for _ in range(K+1)]
stuff = [list(map(int,read().split())) for _ in range(N)]
for w,v in stuff:
    for i in range(K,w-1,-1):
        bag[i] = max(bag[i],bag[i-w]+v)
print(bag[-1])