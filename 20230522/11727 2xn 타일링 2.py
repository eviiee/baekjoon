N = int(input())
D = [0]*(N+1)
D[0] = 1
D[1] = 1
for i in range(2,N+1):
    D[i] = (D[i-1] + (D[i-2] * 2))%10007

print(D[N])