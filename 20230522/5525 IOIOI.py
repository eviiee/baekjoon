N,_,S = int(input()),input(),input().replace('IO','|')
l = []
c = 0
for s in S:
    if c > 0 and s!='|':
        if s == 'I':
            l.append(c)
        elif s == 'O' and c > 1:
            l.append(c-1)
        c = 0
    elif s == '|': c+=1
if c!= 0 : l.append(c-1)
r = 0
for t in l:
    r+=t-N+1 if t>=N else 0
print(r)