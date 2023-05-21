N = int(input())
D = [0]*N
D[0] = 1
D[1] = 2
for i in range(2,N):
    D[i] = D[i-1] + D[i-2]

print(D[-1])