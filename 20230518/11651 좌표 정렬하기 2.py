import sys
print(*[' '.join(line) for line in sorted(list([sys.stdin.readline().split() for _ in range(int(input()))]),key=lambda x: (int(x[1]),int(x[0])))],sep='\n')