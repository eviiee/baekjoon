import sys
read = sys.stdin.readline
N,M=map(int,read().split())
S=set(read() for _ in range(N))
c=0
for _ in range(M): c+=1 if read() in S else 0
print(c)