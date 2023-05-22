import sys
from collections import deque
import time
read = sys.stdin.readline
E = [[(i*2)%10000,i-1 if i>0 else 9999, i//1000+10*(i%1000),i%10*1000+i//10] for i in range(100001)]

def bfs(n,t):
    q = deque([n])
    v = {n:[]}
    while q:
        n = q.popleft()
        for i in range(4):
            x = E[n][i]
            if x not in v:
                v[x] = v[n] + [i]
                if x == t: break
                q.append(x)
        else: continue
        break
    return ''.join(map(lambda x: 'DSLR'[x],v[x]))

# for _ in range(int(read())):
#     a,b = map(int,read().split())
#     r = str(bfs(a,b))
#     sys.stdout.write(r+'\n')
st = time.time()
for i in range(100000):
    for j in range(100000):
        r = str(i)+'=>'+str(j)+'    '+bfs(i,j)+'\n'