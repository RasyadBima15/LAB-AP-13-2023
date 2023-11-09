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

    def being_attack(self,target):
        self._health -= target._power

    # setter
    def setpower(self,npower):
        self._power = npower
    
    def sethealth(self,nhealth):
        self._health = nhealth
    
    def setarmor(self,narmor):
        self._armor = narmor
    
    def setspeed(self,nspeed):
        self._speed = nspeed
    
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



    
    




