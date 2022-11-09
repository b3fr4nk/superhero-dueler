# hero.py
import random


class Hero:
  # We want our hero to have a default "starting_health",
  # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
        name: String
        starting_health: Integer
        current_health: Integer
        '''

        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health

    def fight(self, other_hero):
        '''
        current hero will fight hero passed in
        '''

        rand = random.randint(0, 1)
        if rand == 0:
            print(f"{self.name} beats {other_hero.name}")
        else:
            print(f"{other_hero.name} beats {self.name}")



if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
  hero1 = Hero("Grace Hopper", 200)
  hero2 = Hero("Alan Turing", 220)
  
  hero1.fight(hero2)