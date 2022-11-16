from warrior.classes_warrior.classes import Knight, Barbarian, Adventure, Default
import random
import names


def random_class():
    rand_int = random.randint(1, 3)
    if rand_int == 1:
        return Knight()
    if rand_int == 2:
        return Barbarian()
    if rand_int == 3:
        return Adventure()


class Warrior(Default):
    def __init__(self):
        super().__init__()
        self.warrior_class = random_class().method(self)
        self.name = names.get_full_name()
        self.luck = random.uniform(1.3, 1.9)
        self.confusion = 0
        self.status = "good"

    def __repr__(self, new_warrior):
        return f"Warrior {new_warrior.name} is {new_warrior.title}, with {new_warrior.weapon.name}"

    def rand_luck(self):
        self.luck = random.uniform(1.3, 1.9)
