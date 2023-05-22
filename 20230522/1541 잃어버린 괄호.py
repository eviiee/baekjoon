def main():
    s=input().split('-')
    if len(s) == 1: return sum(list(map(int,s[0].split('+'))))
    for i in range(0,len(s)):
        s[i] = sum(list(map(int,s[i].split('+'))))
    return int(s[0])-sum(list(map(int,s[1:])))
print(main())