# N,r,c=map(int,input().split())
# dr = [0,0,1,1]
# dc = [0,1,0,1]
# def nav(rs,cs,n,v):
#     if n==0 and rs==r and cs==c:
#         print(v)
#         return
#     dn = 2**(n-1)
#     d = 2**(2*n - 2)
#     for i in range(4):
#         nr = rs + dr[i]*dn
#         nc = cs + dc[i]*dn
#         if nr<=r<nr+dn and nc<=c<nc+dn:
#             nav(nr,nc,n-1,v+(d*i))
#     return

# nav(0,0,N,0)



# 재풀이

N,r,c = map(int,input().split())
def find(n,r,c):
    if n == 0 : return 0
    q = 2**(n-1)
    if r < q and c < q : return find(n-1, r, c)
    elif r < q and c >= q : return q**2 + find(n-1, r, c-q)
    elif r >= q and c < q : return 2*(q**2) + find(n-1, r-q, c)
    elif r >= q and c >= q : return 3*(q**2) + find(n-1, r-q, c-q)
print(find(N, r, c))