import random
from ability import Ability

class Weapon(Ability):
    def __init__(self, name, max_damage):
        super().__init__(name, max_damage)

    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        damage = random.randint(self.max_damage//2, self.max_damage)

        return damage