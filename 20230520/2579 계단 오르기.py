import sys
read = sys.stdin.readline

N = int(read())
score =[0] + [int(read()) for _ in range(N)]
s = [[0,0,0] for _ in range(N+1)]
s[1][1] = score[1]
if N > 1:
    s[2][1] = score[2]
    s[2][2] = score[1] + score[2]

for i in range(3,N+1):
    s[i][1] = max(s[i-2][2] + score[i],s[i-2][1]+score[i])
    s[i][2] = s[i-1][1] + score[i]

print(max(s[N][1],s[N][2]))