import sys
import heapq
read = sys.stdin.readline
l = []
for _ in range(int(read())):
    n = int(read())
    if n == 0 : print(heapq.heappop(l)[1] if l else 0)
    else : heapq.heappush(l,(abs(n),n))