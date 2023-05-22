import sys
read = sys.stdin.readline

def main():
    N = int(read())
    B = {i for i in range(10)}
    b = int(read())
    if b > 0 :
        for i in list(map(int,read().split())):
            B.remove(i)
    if abs(100-N) < len(str(N)) or b==10: return abs(100-N)
    up = N
    while abs(up-N)<abs(100-N):
        for i in str(up):
            if int(i) not in B: break
        else:
            up = len(str(up))+abs(up-N)
            break
        up+=1
    else:
        up = abs(100-N)
    down = N
    while abs(down-N)<abs(100-N) and down>=0:
        for i in str(down):
            if int(i) not in B: break
        else:
            down = len(str(down))+abs(down-N)
            break
        down-=1
    else:down = abs(100-N)
    return min(up,down,abs(100-N))
print(main())