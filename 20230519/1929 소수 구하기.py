from math import sqrt,floor
import sys

def isPrime(num):
    if num == 1 : return False
    if num == 2 : return True
    for i in range(2,floor(sqrt(num))+1):
        if num%i == 0: return False
    return True

def main():
    a,b = map(int,input().split())
    if a<=2<=b: print(2)
    nums = [True for _ in range(b+1)]
    for i in range(a-a%2+1,b+b%2,2):
        if nums[i] == True and i>=2:
            for s in range(2,b//i+1): nums[i*s] = False
            if isPrime(i): sys.stdout.write(str(i)+'\n')

main()