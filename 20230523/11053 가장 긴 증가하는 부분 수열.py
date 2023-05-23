input()
N = list(map(int,input().split()))
D = [0] * len(N)

D[0] = 1

for i in range(1,len(N)):
    for j in range(i-1,-1,-1):
        if N[j]<N[i]:
            D[i] = D[j] + 1
            break
    else: D[i] = 1

print(max(D))