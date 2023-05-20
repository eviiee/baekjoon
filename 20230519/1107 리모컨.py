
def main():
    N = int(input())
    M = int(input())
    l = len(str(N))
    B = [True for _ in range(10)]
    if N==100 : return 0
    elif M==10 : return abs(N-100)
    elif M>0:
        for i in list(map(int,input().split())): B[i] = False
    elif M == 0:
        return(min(l,abs(100-N)))
    high = low = N
    while high==low==N:
        

    # 망가진 버튼이 있을 경우 망가진 자릿수마다 위/아래를 조합해 가장 가까운 수를 판단

main()