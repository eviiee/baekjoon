import sys
read = sys.stdin.readline

def init():
    global R,C,S
    read()
    R = read().rstrip().split()
    c = [[' ','w',' '],['g','r','b'],[' ','y',' '],[' ','o',' ']]
    C = [[c[i//3][j//3] for j in range(9)] for i in range(12)]
    S = {'F':(4,4),'U':(1,4),'D':(7,4),'B':(10,4),'L':(4,1),'R':(4,7)}

def rotate(com):
    sur,dir = list(com)
    if sur == 'U':
        if dir == '+':
            C[3],C[-1][3:6] = C[3][3:]+list(reversed(C[-1][3:6])),list(reversed(C[3][:3]))
        if dir == '-':
            C[3],C[-1][3:6] = list(reversed(C[-1][3:6]))+C[3][:6],list(reversed(C[3][6:]))
    elif sur == 'D':
        if dir == '+':
            C[5],C[9][3:6] = list(reversed(C[9][3:6]))+C[5][:6],list(reversed(C[5][6:]))
        if dir == '-':
            C[5],C[9][3:6] = C[5][3:]+list(reversed(C[9][3:6])),list(reversed(C[5][:3]))
    elif sur == 'L':
        if dir == '+':
            s1 = [C[i][3] for i in range(9,12)]
            for i in range(11,2,-1):C[i][3] = C[i-3][3]
            for i in range(3):C[i][3] = s1[i]
        if dir == '-':
            s1 = [C[i][3] for i in range(3)]
            for i in range(9):C[i][3] = C[i+3][3]
            for i in range(9,12):C[i][3] = s1[i-9]
    elif sur == 'R':
        if dir == '-':
            s1 = [C[i][5] for i in range(9,12)]
            for i in range(11,2,-1):C[i][5] = C[i-3][5]
            for i in range(3):C[i][5] = s1[i]
        if dir == '+':
            s1 = [C[i][5] for i in range(3)]
            for i in range(9):C[i][5] = C[i+3][5]
            for i in range(9,12):C[i][5] = s1[i-9]
    elif sur == 'F':
        if dir == '+' :
            lcol,rcol = C[6][3:6],C[2][3:6]
            C[2][3:6],C[6][3:6] = [C[5-i][2] for i in range(3)],[C[5-i][6] for i in range(3)]
            for i in range(3,6): C[i][2],C[i][6] = lcol[i-3],rcol[i-3]
        if dir == '-' :
            lcol,rcol = C[2][3:6],C[6][3:6]
            C[2][3:6],C[6][3:6] = [C[i][6] for i in range(3,6)],[C[i][2] for i in range(3,6)]
            for i in range(3): C[5-i][2],C[5-i][6] = lcol[i],rcol[i]
    elif sur == 'B':
        if dir == '+' :
            for i in range(3,6):
                C[0][i],C[8-i][0],C[8][8-i],C[i][8] = C[i][8],C[0][i],C[8-i][0],C[8][8-i]
        if dir == '-' :
            for i in range(3,6):
                C[0][i],C[8-i][0],C[8][8-i],C[i][8] = C[8-i][0],C[8][8-i],C[i][8],C[0][i]

    cx,cy = S[sur]
    if dir == '-':
        for i in range(2):
            C[cx-1][cy-1+i],C[cx-1+i][cy+1],C[cx+1][cy+1-i],C[cx+1-i][cy-1] = C[cx-1+i][cy+1],C[cx+1][cy+1-i],C[cx+1-i][cy-1],C[cx-1][cy-1+i]
    elif dir == '+':
        for i in range(2):
            C[cx-1][cy-1+i],C[cx-1+i][cy+1],C[cx+1][cy+1-i],C[cx+1-i][cy-1] = C[cx+1-i][cy-1],C[cx-1][cy-1+i],C[cx-1+i][cy+1],C[cx+1][cy+1-i]

def main():
    init()
    for r in R:
        rotate(r)
    print(*[''.join(r[3:6]) for r in C[:3]],sep='\n')

if __name__ == '__main__':
    for _ in range(int(read())):
        main()