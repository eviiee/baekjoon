from collections import deque
import sys
read = sys.stdin.readline

N = int(read())
M = [list(map(int,read().split())) for _ in range(N)]
R = [[0]*N for _ in range(N)]
def bfs(r):
    q = deque([r])
    V = R[r]
    while q:
        v = q.popleft()
        for i in range(N):
            e = M[v][i]
            if e == 1 and V[i] == 0:
                V[i] = 1
                q.append(i)

def main():
    for i in range(N):
        bfs(i)
    print(*[' '.join(list(map(str,row))) for row in R],sep='\n')

main()