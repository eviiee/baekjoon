x=int(input())
t,f=0,0
f+=(x//15)*3
n=x%15
v=False
m=0
for i in range(-1, n//5+1):
    if x==4:break
    nn=n-(5*i)
    if nn%3==0:
        v=True
        m=i
        t=nn//3
f+=m
print(t+f if v else -1)