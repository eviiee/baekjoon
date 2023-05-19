def main():
    N = int(input())
    l = len(str(N))
    for i in range(max(N-(9*l),0),N):
        s = i
        for j in range(l):
            t= (i//(10**j))%10
            s+= t
        if s==N: return i
    return 0
print (main())