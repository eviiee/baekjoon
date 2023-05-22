N = int(input())
D = [[0,0] for _ in range(N+1)]
for i in range(1,N+1):
    t = i
    c = 0
    while t%2 == 0:
        c+=1
        t//=2
    D[i][0] = D[i-1][0]+c
    t = i
    c = 0
    while t%5 == 0:
        c+=1
        t//=5    
    D[i][1] = D[i-1][1]+c
print(min(D[-1][0],D[-1][1]))