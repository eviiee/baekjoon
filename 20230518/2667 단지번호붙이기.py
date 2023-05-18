import sys
from collections import deque
read=sys.stdin.readline

n=int(read())
map=[list(map(int,list(read().strip()))) for _ in range(n)]

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def main():
    
    houseCounts=[]
    for r in range(n):
        for c in range(n):
            if map[r][c] != 0:
                map[r][c] = 0
                houseCounts.append(bfs((r,c)))
    houseCounts.sort()
    print(len(houseCounts))
    print(*houseCounts,sep='\n')

def bfs(pos):
    
    countingHouse = deque([pos])
    housecounts=1
    
    while countingHouse:
        x,y=countingHouse.popleft()
        adjs = [(x+dx[i],y+dy[i]) for i in range(4)]
        for nx,ny in adjs:
            if 0<=nx<n and 0<=ny<n and map[nx][ny] == 1:
                map[nx][ny]=0
                housecounts+=1
                countingHouse.append((nx,ny))

    return housecounts

main()