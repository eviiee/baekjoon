N = int(input())
M = N**0.5

def main():
    if M.is_integer() : return 1
    for i in range(1,int(M)+1):
        if ((N-i**2)**0.5).is_integer() : return 2
    for i in range(1,int(M)+1):
        for j in range(1,int((N-i**2)**0.5)+1):
            if ((N-i**2-j**2)**0.5).is_integer() : return 3
    else : return 4

print(main())