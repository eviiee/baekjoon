X = '666'
def find(n):
    x = 666
    c = 0
    i = 0
    while c<n:
        if X in str(x+i): c+=1
        i+=1
    return x+i-1
print(find(int(input())))
