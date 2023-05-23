import sys
read = sys.stdin.readline

def init():
    global myhero,gameon,rpgmap,moves,minimap,N,M
    N,M = map(int,read().split())
    rpgmap = [['.']*(M+1)]
    minimap = [[None]*(M+1) for _ in range(N+1)]
    K = 0
    I = 0
    for i in range (N):
        r = list(read().rstrip())
        for j in range(M):
            c = r[j]
            if c == '&': K+=1
            elif c == '@': myhero = hero(i+1,j+1)
            elif c == '^': minimap[i+1][j+1] = spike()
            elif c == 'B': I+=1
        rpgmap.append(['.']+r)
    moves = list(read().rstrip())
    for _ in range(K+1):
        r,c,s,w,a,h,e = read().split()
        r,c,w,a,h,e = int(r),int(c),int(w),int(a),int(h),int(e)
        minimap[r][c] = monster(s,w,a,h,e,rpgmap[r][c]=='M')
    for _ in range(I):
        r,c,t,e = read().split()
        r,c = int(r),int(c)
        if t == 'W': i = weapon(int(e))
        elif t == 'A': i = armor(int(e))
        elif t == 'O': i = acc(e)
        minimap[r][c] = i
    gameon = True
    return

def gameOver():
    global gameon
    gameon = False
    return

class hero():
    def __init__(self,r,c):
        self.maxhp = 20
        self.hp = 20
        self.atk = 2
        self.dfs = 2
        self.lvl = 1
        self.exp = 0
        self.o_slot = set()
        self.weapon = weapon(0)
        self.armor = armor(0)
        self.init_pos = (r,c)
        self.cur_pos = [r,c]

    def getExp(self,gained_exp):
        if 'EX' in self.o_slot : gained_exp*=1.2
        if 'HR' in self.o_slot :
            if self.maxhp - self.hp >= 3 : self.hp+=3
            else : self.hp = self.maxhp
        self.exp += int(gained_exp)
        if self.exp >= self.lvl * 5:
            self.lvl+=1
            self.exp = 0
            self.maxhp += 5
            self.atk += 2
            self.dfs +=2
            self.hp = self.maxhp

    def equip(self,equpiment):
        if type(equpiment) == weapon:
            self.atk -= self.weapon.atk
            self.atk += equpiment.atk
            self.weapon = equpiment
        elif type(equpiment) == armor:  
            self.dfs -= self.armor.dfs
            self.dfs += equpiment.dfs
            self.armor = equpiment
        elif type(equpiment) == acc:
            if equpiment.type not in self.o_slot and len(self.o_slot) < 4:
                self.o_slot.add(equpiment.type)

    def getDmg(self,attacker,firstattack=False):
        
        if type(attacker) == monster:
            if not (attacker.isboss and 'HU' in self.o_slot and firstattack):
                self.hp -= max(1,attacker.atk - self.dfs)
            else:
                self.hp = self.maxhp
        elif type(attacker) == spike:
            if 'DX' in self.o_slot : self.hp -= 1
            else : self.hp -= 5
        if self.hp <= 0:
            if 'RE' in self.o_slot :
                self.hp = self.maxhp
                if type(attacker) == monster : attacker.hp = attacker.maxhp
                self.moveTo(self.init_pos)
                self.o_slot.remove('RE')
                return True
            else :
                self.hp = 0 
                self.die()
                gameOver()
                return True
        else: return False
    
    def battle(self,_monster):
        global gameon
        firstattack = self.atk
        if 'CO' in self.o_slot and 'DX' not in self.o_slot: firstattack*=2
        elif 'CO' in self.o_slot and 'DX' in self.o_slot: firstattack*=3
        hero_win =  _monster.getDmg(firstattack)
        firstattack = True
        if not hero_win:
            while True:
                monster_win = self.getDmg(_monster, firstattack)
                if firstattack : firstattack = False
                if monster_win : break
                hero_win = _monster.getDmg(self.atk)
                if hero_win : break
        if hero_win : self.getExp(_monster.exp)
        return self if hero_win else _monster

    def moveTo(self,pos):
        x,y = pos
        w = minimap[x][y]
        if w == None:
            self.updateMap(x,y)
            return
        elif type(w) == monster :
            winner = self.battle(w)
            if winner == w and not gameon:
                return f'YOU HAVE BEEN KILLED BY {w.name}..'
            
            elif winner == self:
                self.updateMap(x,y)
                if w.isboss:
                    gameOver()
                    return 'YOU WIN!'
        elif type(w) == spike :
            self.updateMap(x,y)
            self.getDmg(w)
            if not gameon : return 'YOU HAVE BEEN KILLED BY SPIKE TRAP..'
        else :
            self.equip(w)
            self.updateMap(x,y)
        return
    
    def updateMap(self,x,y):
        stepping_on = type(minimap[self.cur_pos[0]][self.cur_pos[1]])
        if stepping_on == spike: rpgmap[self.cur_pos[0]][self.cur_pos[1]] = '^'
        else : rpgmap[self.cur_pos[0]][self.cur_pos[1]] = '.'
        rpgmap[x][y] = '@'
        w = type(minimap[x][y])
        if w != spike: minimap[x][y] = None
        self.cur_pos = [x,y]
        return
    
    def die(self):
        cx,cy = self.cur_pos
        if type(minimap[cx][cy]) == spike : rpgmap[cx][cy] = '^'
        else : rpgmap[cx][cy] = '.'
        return


class weapon():
    def __init__(self,dmg):
        self.atk = dmg

class armor():
    def __init__(self,dfs):
        self.dfs = dfs

class acc():
    def __init__(self,type):
        self.type = type

class spike():
    def __init__(self):
        pass

class monster():
    
    def __init__(self,name,atk,dfs,hp,exp,isboss):
        self.name = name
        self.atk = atk
        self.dfs = dfs
        self.maxhp = hp
        self.hp = hp
        self.exp = exp
        self.isboss = isboss

    def getDmg(self,dmg):
        self.hp -= max(1,dmg-self.dfs)
        if self.hp <= 0 :return True
        return False

def main():
    init()
    m = {'R':[0,1],'L':[0,-1],'U':[-1,0],'D':[1,0]}
    turn = 0
    while gameon and turn<len(moves):
        move = moves[turn]
        x,y = myhero.cur_pos
        nx = x + m[move][0]
        ny = y + m[move][1]
        if not ( 0<nx<=N and 0<ny<=M and rpgmap[nx][ny] != '#') : nx,ny = x,y
        msg = myhero.moveTo((nx,ny))
        turn+=1
    print(*[''.join(row[1:]) for row in rpgmap[1:]],sep='\n')
    print(f'Passed Turns : {turn}')
    print(f'LV : {myhero.lvl}')
    print(f'HP : {myhero.hp}/{myhero.maxhp}')
    print(f'ATT : {myhero.atk - myhero.weapon.atk}+{myhero.weapon.atk}')
    print(f'DEF : {myhero.dfs - myhero.armor.dfs}+{myhero.armor.dfs}')
    print(f'EXP : {myhero.exp}/{myhero.lvl*5}')
    print(msg if msg != None else 'Press any key to continue.')


if __name__ == '__main__':
    main()