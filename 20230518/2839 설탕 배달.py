# n=int(input())

def main(n):
    t,f=0,0
    f+=(n//15)*3
    n%=15
    v=False
    m=0
    for i in range(n//5+1):
        nn=n-(5*i)
        if nn%3==0:
            v=True
            m=i
            t=nn//3
    f+=m
    print(t+f if v else -1)

for i in range(3,19):
    main(i)