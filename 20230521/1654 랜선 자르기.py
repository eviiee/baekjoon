import sys
read = sys.stdin.readline

K,N = map(int,read().rstrip().split())
l = [int(read()) for _ in range(K)]
l.sort()

st = 0
ed = l[-1]
ln = 0
while st<ed:
    ln = (st+ed+1)//2
    n = sum([x//ln for x in l])
    if n<N: ed = ln - 1
    elif n>=N: st = ln

print(st)