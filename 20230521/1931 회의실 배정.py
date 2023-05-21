import sys
read=sys.stdin.readline
M=[list(map(int,read().split())) for _ in range(int(read()))]
M.sort(key=lambda x: (x[1],x[0]))
c=0
t = 0
for i in M:
    if i[0]>=t :
        c+=1
        t=i[1]

print(c)