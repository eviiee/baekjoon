import sys
h={}
def m(k):
    n,a,b = k
    if n==1 :
        return(f'{a} {b}')
    if k in h : return h[k]
    r='\n'.join([
        m((n-1,a,6-a-b)),  
        m((1,a,b)),
        m((n-1,6-a-b,b))
    ])
    h[k] = r
    return r
N = int(input())
print(2**N-1)
if N<=20 : sys.stdout.write(m((N,1,3)))