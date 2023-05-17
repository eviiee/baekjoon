n=lambda x:ord(x)-ord('a')+1
input()
r=0
s=input()
for i in range(len(s)):
    r=(r+(n(s[i])*(31**i)))%1234567891
print(r)