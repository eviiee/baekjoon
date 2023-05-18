n,h=map(int,input().split())
trees=sorted(list(map(int,input().split())),reverse=True)

# woods=0
# height=trees[0]
# i=0


i,j=0,n
k=None
while trees[k]*h<=j:
    k=n//2
    if htrees[k]:
        while trees[k+1]==h:k+=1
        break
    elif trees[k]>=height:i=k+1
    else: j=k-1

while True:
    
    while trees[i]>height:i+=1


