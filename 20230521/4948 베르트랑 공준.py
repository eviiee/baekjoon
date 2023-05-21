import sys
read=sys.stdin.readline

P=[True for _ in range(123456*2+1)]
P[:2]=[False,False]

for i in range(2,len(P)):
    if P[i]:
        for j in range(2*i,len(P),i):P[j]=False

while True:
    n=int(read())
    if n == 0 : break
    print(P[n+1:2*n+1].count(True))