import sys
read=sys.stdin.readline

p=''.join([['WB','BW'][(i//4)%2] for i in range(32)])

compare=lambda x,y:sum([1 if x[i]!=y[i] else 0 for i in range(64)])

N,M = map(int,read().split())
board=[read().rstrip() for _ in range(N)]
change=64
for r in range(N-7):
    arr=board[r:r+8]
    for c in range(M-7):
        l=''.join([row[c:c+8] for row in arr])
        n=compare(p,l)
        change=min(change,n,64-n)
print(change)