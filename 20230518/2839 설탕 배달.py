def main():
    N = int(input())
    c = [[-1,0] for _ in range(N+1)]
    c[0][0] = 0
    
    for i in range(3,N+1):
        if c[i-2][0] == c[i-3][0] == c[i-5][0] == -1 : continue
        if c[i-2][0] > 0:
            c[i][0] = c[i-2][0] - 1
            c[i][1] = c[i-2][1] + 1
        elif c[i-5][0] != -1 :
            c[i][0] = c[i-5][0]
            c[i][1] = c[i-5][1] + 1
        elif c[i-3][0] != -1 :
            c[i][0] = c[i-3][0] + 1
            c[i][1] = c[i-3][1]

    return sum(c[N])

print (main())