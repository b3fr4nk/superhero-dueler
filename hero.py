from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
  # We want our hero to have a default "starting_health",
  # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
            abilities: List
            armors: List
            name: String
            starting_health: Integer
            current_health: Integer
        '''

        #kills and deaths start at 0
        self.deaths = 0
        self.kills = 0

        # abilities and armors don't have starting values,
        # and are set to empty lists on initialization
        self.abilities = list()
        self.armors = list()
        self.weapons = list()

        # we know the name of our hero, so we assign it here
        self.name = name

        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health

        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health

    def add_ability(self, ability):
        ''' Add ability to abilities list '''

        self.abilities.append(ability)

    def add_weapon(self, weapon):
        '''Add weapon to self.abilities'''

        self.weapons.append(weapon)

    def attack(self):

        total_damage = 0
        #loop through all of the heroes abilities
        for ability in self.abilities:
            #use abilities and add damage to total damage
            total_damage += ability.attack()
        for weapon in self.weapons:
            total_damage += weapon.attack()
        #return total_damage
        return total_damage

    def add_armor(self, armor):
        ''' Add ability to abilities list '''

        self.armors.append(armor)

    def defend(self):
        '''
        Calculate the total block amount from all armor blocks.
        return: total_block:Int
        '''

        total_defended = 0

        for armor in self.armors:
            total_defended += armor.block()

        return total_defended

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.'''
        
        defence = self.defend()
        damage -= defence
        self.current_health -= damage

        print(f"{self.name} took {damage} damage")


    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not.'''

        # if hero's health is <= 0, then return False. Otherwise, they still have health
        if self.current_health <= 0:
            return False
        # and are therefore alive, so return True
        else:
            return True

    def add_kill(self):
        self.kills += 1

    def add_death(self):
        self.deaths += 1

    def fight(self, opponent):
        '''Current Hero will take turns fighting the opponent hero passed in.'''

        if len(self.abilities) != 0 and len(opponent.abilities) != 0:
            while True:
                self.take_damage(opponent.attack())
                if not self.is_alive():
                    print(f"{opponent.name} has won")
                    self.add_death()
                    opponent.add_kill()
                    return opponent

                opponent.take_damage(self.attack())
                if not opponent.is_alive():
                    print(f"{self.name} has won")
                    self.add_kill()
                    opponent.add_death()
                    return self
                
        else:
            print("Draw")
            if len(self.abilities) != 0 and len(opponent.abilities) == 0:
                opponent.current_health = 0
                print(f"{self.name} has won")
                self.add_kill()
                opponent.add_death()
                return self
            elif len(self.abilities) == 0 and len(opponent.abilities) != 0:
                self.current_health = 0
                print(f"{opponent.name} has won")
                self.add_death()
                opponent.add_kill()
                return opponent




if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)