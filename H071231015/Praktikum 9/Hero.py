class Human:
    def __init__(self, name, pos_x):
        self.name = name
        self.__pos_x = pos_x
        self._get_speed = 0

    def movement(self, arah):
        if arah == "L":
            self.__pos_x -= self.get_speed
        elif arah == "R":
            self.__pos_x += self.get_speed

    def get_pos_x(self):
        return self.__pos_x

    def set_pos_x(self, pos_x):
        self.__pos_x = pos_x


class Hero(Human):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._get_speed = 3

    def get_health(self):
        return self._health
    
    def set_health(self, health):
        self._health = health

    def attack(self, target):
        target.set_health(target.get_health() - self._power)


class Warrior(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 26
        self._armor = 30

    def special(self, target):
        self._armor = 45
        self._power = 32
        self.attack(target)


class Assassin(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 35
        self.get_speed = 4

    def special(self, target):
        self.get_speed = 7
        self._power = 42
        self.attack(target)


class Support(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._health = 500
        self._armor = 8
        self.get_speed = 4

    def special(self, target):
        self.get_speed = 6
        target.set_health(target.get_health() + 150)



