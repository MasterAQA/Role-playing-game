from warrior.classes_warrior.human import *
import random
from warrior.weapons.weapons import *


def random_weapon():
    rand_int = random.randint(1, 3)
    if rand_int == 1:
        sword = Sword()
        return sword
    if rand_int == 2:
        axe = Axe()
        return axe
    if rand_int == 3:
        mace = Mace()
        return mace


class Default(Human):
    def __init__(self):
        super().__init__()
        self.title = "Default"
        self.weapon = random_weapon()


class Knight(Human):
    def __init__(self):
        super().__init__()
        self.weapon = random_weapon()

    def method(self, obj):
            obj.title = "Knight"
            obj.health += 50
            obj.armor += 50
            obj.speed -= 0.5


class Barbarian(Human):
    def __init__(self):
        super().__init__()
        self.weapon = random_weapon()

    def method(self, obj):
        obj.title = "Barbarian"
        obj.health += 30
        obj.armor += 20
        obj.speed += 1


class Adventure(Human):
    def __init__(self):
        super().__init__()
        self.weapon = random_weapon()

    def method(self, obj):
        obj.title = "Adventure"
        obj.health += 20
        obj.armor += 30
        obj.speed += 0.5

