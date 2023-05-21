
N = int(input())
D = sorted(list(map(int,input().split())))
for i in range(1,N):D[i] += D[i-1]
print(sum(D))