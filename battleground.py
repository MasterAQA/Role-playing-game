import random
import sys

from warrior.warriors import Warrior


def hit(warrior_1, warrior_2):
    """Наносит удар Warrior_1"""
    warrior_1.rand_luck()
    damage = (warrior_1.weapon.damage * warrior_1.luck)
    if damage > (warrior_1.weapon.damage * 1.8):
        damage = damage * 1.5
    if damage < (warrior_1.weapon.damage * 1.4):
        damage = 0

    if warrior_2.armor <= 5:
        warrior_2.health -= damage
    else:
        warrior_2.armor -= damage

    stun_damage = (warrior_1.weapon.stun * warrior_1.luck / warrior_2.speed)
    if stun_damage < (warrior_1.weapon.stun * 1.4 / warrior_2.speed):
        warrior_2.confusion += 0
    else:
        warrior_2.confusion += stun_damage

    if warrior_2.confusion >= 10:
        warrior_2.status = 'bad'
        print(f"{warrior_1.name} нанёс {damage} урона, игрока {warrior_2.name} застанили.")

    elif damage > (warrior_1.weapon.damage * 1.7):
        print(f"{warrior_1.name} сделал критический удар! Нанесено {damage} урона")

    elif stun_damage < (warrior_1.weapon.stun * 1.4 / warrior_2.speed):
        print(f"{warrior_1.name} повезло, в последний момент он увернулся и получил {damage} урона")

    else:
        print(f"{warrior_1.name} нанёс {damage} урона")



def who_win():
    if warrior_1.health < 0:
        print("")
        print(
            f"В дуэли победил {warrior_2.name}! Его звание {warrior_2.title}, с оружием {warrior_2.weapon.name}")
        sys.exit()
    elif warrior_2.health < 0:
        print("")
        print(
            f"В дуэли победил {warrior_1.name}! Его звание {warrior_1.title}, с оружием {warrior_1.weapon.name}")
        sys.exit()



def run_war(new_battle):
    if new_battle.first == "warrior_1":
        while warrior_1.health > 0 or warrior_2.health > 0:
            new_battle.check_status()
            hit(warrior_2, warrior_1)
            who_win()
            new_battle.check_status()
            hit(warrior_1, warrior_2)
            who_win()

            print(f"У {warrior_1.name} осталось ХП {warrior_1.health} и {warrior_1.armor} щита")
            print(f"У {warrior_2.name} осталось ХП {warrior_2.health} и {warrior_2.armor} щита")
            print("")


    if new_battle.first == "warrior_2":
        while warrior_1.health > 0 or warrior_2.health > 0:
            new_battle.check_status()
            hit(warrior_1, warrior_2)
            who_win()

            new_battle.check_status()
            hit(warrior_2, warrior_1)
            who_win()

            print(f"У {warrior_1.name} осталось ХП {warrior_1.health} и {warrior_1.armor} щита")
            print(f"У {warrior_2.name} осталось ХП {warrior_2.health} и {warrior_2.armor} щита")
            print("")



class Battle:
    def __init__(self, warrior_1, warrior_2):
        self.first = ""
        self.warrior_1 = warrior_1
        self.warrior_2 = warrior_2


    def who_first(self):
        rand = random.randint(1, 2)
        if rand == 1:
            hit(warrior_1, warrior_2)
            self.first = "warrior_1"
        elif rand == 2:
            hit(warrior_2, warrior_1)
            self.first = "warrior_2"


    def check_status(self):
        if warrior_2.status == "bad":
            warrior_2.status = "good"
            warrior_2.confusion = 0
            hit(warrior_1, warrior_2)


        if warrior_1.status == "bad":
            warrior_1.status = "good"
            warrior_1.confusion = 0
            hit(warrior_2, warrior_1)






if __name__ == "__main__":
    warrior_1 = Warrior()
    print(f"Warrior №1 - " + warrior_1.__repr__(warrior_1))

    print("")

    warrior_2 = Warrior()
    print(f"Warrior №2 - " + warrior_2.__repr__(warrior_2))

    print("")

    new_battle = Battle(warrior_1, warrior_2)
    new_battle.who_first()
    run_war(new_battle)













