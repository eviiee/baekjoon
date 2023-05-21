N = int(input())
x = list(map(int,input().split()))
s = list(sorted(set(x)))
c = {}
for i in range(len(s)):
    c[s[i]] = i

for ix in x:print(c[ix],end=' ')