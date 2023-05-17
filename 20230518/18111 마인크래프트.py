import sys
from collections import Counter
read=sys.stdin.readline

N,M,I=map(int,read().rstrip().split())

land = []
for _ in range(N):land.extend(list(map(int,read().rstrip().split())))
land = Counter(land)
heights = set(land.keys())

highest=max(heights)
lowest=min(heights)

shortest=[-1,highest]
for height in range(lowest, highest+1):
    highs=lows=0
    for h in heights:
        d = h - height
        if d>0: highs+=land[h]*d
        elif d<0 : lows+=-land[h]*d
    if highs+I>=lows:
        time=2*highs+lows
        if shortest[0]==-1:shortest=[time,height]
        elif shortest[0]>time: shortest=[time,height]
        elif shortest[0]==time: shortest[1]=max(shortest[1],height)

print(f'{shortest[0]} {shortest[1]}')