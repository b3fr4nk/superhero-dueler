import random
from hero import Hero
from team import Team
from weapon import Weapon
from ability import Ability
from armor import Armor

team_one = Team("One")
jodie = Hero("Jodie Foster")
aliens = Ability("Alien Friends", 10000)
jodie.add_ability(aliens)
team_one.add_hero(jodie)
team_two = Team("Two")
athena = Hero("Athena")
socks = Armor("Socks", 10)
athena.add_armor(socks)
team_two.add_hero(athena)

team_one.attack(team_two)