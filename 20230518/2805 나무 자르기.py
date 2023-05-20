n,h=map(int,input().split())
trees=sorted(list(map(int,input().split())),reverse=True)

x = 0
y = trees[0]

while x < y:
    m = (x+y)//2
    l = list(filter(lambda x: x>=m, trees))
    s = sum(l)
    print(x,y,m,l,s)
    if s - m*n > h : x = m
    elif s - m*n < h : y = m
    elif s - m*n == h : break

print (m)