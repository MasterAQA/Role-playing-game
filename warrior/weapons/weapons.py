from warrior.weapons.weapon import Weapon

class Mace(Weapon):
    def __init__(self):
        self.name = "Mace"
        self.damage = 6
        self.stun = 5

class Sword(Weapon):
    def __init__(self):
        self.name = "Sword"
        self.damage = 10
        self.stun = 1

class Axe(Weapon):
    def __init__(self):
        self.name = "Axe"
        self.damage = 8
        self.stun = 3
