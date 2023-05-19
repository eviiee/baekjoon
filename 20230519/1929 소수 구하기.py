def main():
    a,b = map(int,input().split())
    if a<=2<=b: print(2)
    isprime = [True] * (b+1)
    for i in range(3,b+b%2,2):
        for s in range(2,b//i+1): isprime[i*s] = False
        if isprime[i] and i>=a: print(i)
main()