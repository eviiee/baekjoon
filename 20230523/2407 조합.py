a,b = map(int,input().split())
r=1
for i in range(a,a-b,-1):
    r*=i
for i in range(1,b+1):
    r//=i
print(r)