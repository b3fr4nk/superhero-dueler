import random
from hero import Hero

class Team:
    def __init__(self, name):
        
        self.name = name
        self.heroes = list()

    def remove_hero(self, hero_name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        
        found_hero = False

        for hero in self.heroes:
            if hero.name == hero_name:
                self.heroes.remove(hero_name)

                found_hero = True

        if not found_hero:
            return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console.'''

        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        ''' Add Hero object to self.heroes '''

        self.heroes.append(hero)

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''

        for hero in self.heroes:
            hero.current_health = hero.starting_health * health/100

    def attack(self, other_team):
        ''' Battle each team against each other.'''

        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            your_hero = random.choice(living_heroes)
            opponent_hero = random.choice(living_opponents)

            winner = your_hero.fight(opponent_hero)

            if winner == your_hero:
                living_opponents.remove(opponent_hero)
                print(f"Your team: {living_heroes}\nEnemy team: {living_opponents}")
            elif winner == opponent_hero:
                living_heroes.remove(your_hero)
                print(f"Your team: {living_heroes}\nEnemy team: {living_opponents}")
            
    def stats(self):

        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f"{hero.name} Kills/Deaths:{kd}")