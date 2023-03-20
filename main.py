from random import*
# voir : https://www.pkmn.help/defense/?mode=solo&types=normal&format=simple
TYPE = {'normal' : [["combat"], [], ["spectre"]],
        "combat" : [["vol", "psy", "fee"], ["roche", "insecte", "tenebres"], []],
        "vol" : [["roche", "electrik", "glace"], ["combat", "insecte", "plante"], ["sol"]],
        "poison" : [["sol", "psy"], ["combat", "poison", "insecte", "plante", "fee"], []],
        "sol" : [["eau", "plante", "glace"], ["poison", "roche"], ["electrik"]],
        "roche" : [["combat", "sol", "acier", "eau", "plante"], ["normal", "vol", "poison", "feu"], []],
        "insecte" : [["vol", "roche", "feu"], ["combat", "sol", "plante"], []],
        "spectre" : [["spectre", "tenebres"], ["poison", "insecte"], ["normal", "combat"]],
        "acier" : [["combat", "sol", "feu"], ["normal", "vol", "roche", "insecte", "acier", "plante", "psy", "glace", "dragon", "fee"], ["poison"]],
        "feu" : [["sol", "roche", "eau"], ["insecte", "acier", "feu", "plante", "glace", "fee"],[]],
        "eau" : [["plante", "electrik"], ["acier", "feu", "eau", "glace"], []],
        "plante" : [["vol", "poison", "insecte", "feu", "glace"], ["sol", "eau", "plante", "electrik"], []],
        "electrik" : [["sols"], ["vol", "acier", "electrik"], []],
        "psy" : [["insecte", "spectre", "tenebre"], ["combat", "psy"], []],
        "glace" : [["combat", "roche", "acier", "feu"], ["glace"], []],
        "dragon" : [["glace", "dragon", "fee"], ["feu", "eau", "plante", "electrik"], []],
        "tenebres" : [["combat", "insecte", "fee"], ["spectre", "tenebres"], ["psy"]],
        "fee" : [["poison", "acier"], ["combat", "insecte", "tenebres"], ["dragon"]]}


class pokemon:
    def __init__(self, name : str, hp : int, lvl : int, ATK : int, DEF : int = 0, element : str = "normal"):
        self._name = name
        self._hp = hp
        self.lvl = lvl
        self.ATK = ATK
        self.DEF = DEF
        self.elm = element


class team:
    def __init__(self):
        self.liste = []
    def pokeadd(self, p):
        if self.liste < 6:
            self.liste.append(p)
        else:
            print("choose one pokemon to remove :")
            for a in self.liste:
                print(a)
            P = input()
            if P not in self.liste:
                print("wrong name")
            else:
                self.liste.remove(P)
                self.liste.append(p)


class Combat:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.atk1 = 0
        self.atk2 = 0
    def verifie(self):
        if self.p1._hp <= 0:print(self.p1.name + " is out!")
        if self.p2._hp <= 0:print(self.p2.name + " is out!")
    def winner(self):
        if self.p1._hp <= 0:print(self.p2.name + " has won!")
        if self.p2._hp <= 0:print(self.p1.name + " has won!")
    def pimp(self):
        self.atk = randrange(0,2)
    def check(self, n : int):
        if n == 1:
           n = 2
        elif n == 2:
            n = 1
        else:
            return "wrong number, only 1 for p1 and 2 for p2"
        if eval("self.p"+str((n+1)%2+1)+".elm") in eval("TYPE['self.p"+str(n%2+1)+".elm'][0]"):
            eval("self.p"+str(n%2+1)+"._hp -= self.p"+str((n+1)%2+1)+".ATK *2")
        elif eval("self.p"+str((n+1)%2+1)+".elm") in eval("TYPE['self.p"+str(n%2+1)+".elm'][1]"):
            eval("self.p"+str(n%2+1)+"._hp -= self.p"+str((n+1)%2+1)+".ATK *1/2")
        elif eval("self.p"+str((n+1)%2+1)+".elm") not in eval("TYPE['self.p"+str(n%2+1)+".elm'][2]"):
            eval("self.p"+str(n%2+1)+"._hp -= self.p"+str((n+1)%2+1)+".ATK")
        
        

""" je suis deg parce que cette fonction était trop bien :/
def fight(p1, p2, turn : int = 0):
    if p1.hp <= 0:
        print(p2.name + " has won!")
    elif p2.hp <= 0:
        print(p1.name + " has won!")
    elif randrange(0,2):
        fight(p1, p2, turn+1)
    else:
        if turn%2:
            if p2.elm in TYPE[p1.elm][0]:
                p1.hp -= p2.ATK*2
            elif p2.elm in TYPE[p1.elm][1]:
                p1.hp -= p2.ATK//2
            elif p2.elm in TYPE[p1.elm][2]:
                pass
            else:
                p1.hp -= p2.ATK
        else:
            if p1.elm in TYPE[p2.elm][0]:
                p2.hp -= p1.ATK*2
            elif p1.elm in TYPE[p2.elm][1]:
                p2.hp -= p1.ATK//2
            elif p1.elm not in TYPE[p2.elm][2]:
                p2.hp -= p1.ATK
        fight(p1, p2, turn+1)
"""
