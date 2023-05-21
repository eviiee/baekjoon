from sys import stdin
read=stdin.readline
D = [0] * 12
D[0] = 1
for i in range(1,12):
    D[i] = sum([D[i-j] if i>=j else 0 for j in range(1,4)])
for _ in range(int(read())):
    print(D[int(read())])