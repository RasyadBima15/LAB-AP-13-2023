class Human:
    def __init__(self,nama,pos_x,speed=1) :
        self.nama = nama
        self.__position = pos_x
        self._speed = speed

    def movement (self,arah) :
        self.movement = arah
        if arah.upper() == "L" :
            self.__position = self.__position - self._speed
        elif arah.upper() == "R" :
            self.__position = self.__position + self._speed

    #set key
    def setspeed (self,newspeed) :
        self._speed = newspeed            
    def setpos_x (self,pos_x) :
        self.__position = pos_x 

    #get key
    def getspeed (self) :
        return self._speed
    def getpos_x (self) :
        return self.__position
    
class Hero(Human) :
    def __init__(self,nama,pos_x) :
        super().__init__(nama,pos_x)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3


    def attack(self,target)  :
        target._health = target._health - self._power
        return target._health
    
    #get key
    def gethealth(self) :
        return self._health
    def getspeed(self) :
        return self._speed
    def getarmor(self):
        return self._armor
    
    #set key
    def sethealth(self, health):
        self._health = health
    def setspeed(self, speed):
        self._speed = speed
    def setarmor(self, armor):
        self._armor = armor

class Warrior (Hero) :
    def __init__(self,nama,pos_x) :
        super().__init__(nama,pos_x)
        self._power = 26
        self._armor = 30

    def special(self,target) :
        self._power = 32
        self._armor = 45
        target._health = target._health - self._power

class Assassin (Hero) :
    def __init__(self,nama,pos_x) :
        super().__init__(nama,pos_x)
        self._power = 35
        self._speed = 4

    def special(self,target):
        self._power = 42
        self._speed = 7
        target._health = target._health - self._power


class Support (Hero) :
    def __init__(self,nama,pos_x) :
        super().__init__(nama,pos_x)
        self._health = 500
        self._armor = 8
        self._speed = 4

    def special(self,target) :
        self._speed = 6
        target._health = target._health + 150

warrior = Warrior("bambang", pos_x = 10)
assassin = Assassin("joko", pos_x= 25)
support = Support("udin",pos_x= 30)
# sebelum
print("health (before)", warrior.gethealth())
assassin.attack(warrior)
# sesudah
print("health (after)", warrior.gethealth())
print("-"*10)
# sebelum
print("Warrior (health)", warrior.gethealth())
print("Support (speed) : ",support.getspeed())
support.special(warrior)
# sesudah
print("Warrior (health)", warrior.gethealth())
print("Support (speed): ",support.getspeed())
print("-"* 10)
assassin.movement("r")
print("posisi Assassin sekarang adalah : " ,assassin.getpos_x())

print(assassin._speed)
