n,h=map(int,input().split())
trees=sorted(list(map(int,input().split())))

st = 0
ed = trees[-1]

while st < ed:
    ht = (st+ed+1)//2
    s = sum([tree-ht if tree>=ht else 0 for tree in trees])
    if s>=h: st=ht
    elif s<h: ed = ht - 1

print (st)