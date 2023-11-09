class Human:
    def __init__(self, name, pos_x):
        self.name = name
        self.__position = pos_x
        self._speed = 4

    def movement(self, arah):
        if arah == "R" or arah == "r":
            self.__position += self._speed
        elif arah == "L" or arah == "l":
            self.__position -= self._speed

    def getmovement(self):
        print(self.__position)

    def setposition(self,posisi):
        self.__position = posisi

class Hero(Human):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3
    
    def Attack(self,target):
        print(self.name +" attacking " + target.name)
        target.being_attack(self)

    #setter
    def being_attack(self,target):
        self._health -= target._power

    #getter
    def gethealth(self):
        return self._health

    def getpower(self):
        return self._power

    def getarmor(self):
        return self._armor

    def getspeed(self):
        return self._speed


class Warrior(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 26
        self._armor = 30

    def Warrior_special(self,target):
        self._armor = 45
        self._power = 32
        print(self.name +" use special attack ")
        self.Attack(target)

class Assasins(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 35
        self.speed = 4

    def Assasins_special(self,target):
        self._power = 42
        self.speed = 7
        print(self.name +" use special attack ")
        self.Attack(target)

class Support(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._health = 500
        self._armor = 8
        self._speed = 4
        
    def Support_special(self,target):
        self._speed = 6
        print(self.name +" use heal to " + target.name)
        target._health += 150

# garen = Warrior("garen",pos_x=30)
# yasuo = Assasins("yasuo",pos_x=30)
# sora = Support("sora", pos_x=30)

# garen.gethealth()
# yasuo.Assasins_special(garen)
# garen.gethealth()
# sora.Support_special(garen)
# garen.gethealth()


warrior = Warrior("bambang", pos_x=10)
assassin = Assasins("joko", pos_x=25)
support = Support("udin",pos_x=30)
# sebelum
print("health (before)", warrior.gethealth())
assassin.Attack(warrior)
# sesudah
print("health (after)", warrior.gethealth())
print("-"*10)
# sebelum
print("Warrior (health)", warrior.gethealth())
print("Support (speed) : ",support.getspeed())
support.Support_special(warrior)
# sesudah
print("Warrior (health)", warrior.gethealth())
print("Support (speed): ",support.getspeed())

    
    




