import pygame
import random
from Monster import Monster

def monster_spawner(group_monstre, map_with, map_height,list_wall,home):
    x = random_spawn(map_with)
    y = random_spawn(map_height)
    monster = Monster(x,y,list_wall,home) # Creer 1 monstre
    group_monstre.add(monster) # L'ajoute au groupe

def random_spawn(max):
    # Randomiser le spawn entre 0 et 500 et 1500 et 2000
    if random.randint(0,1) == 0:
        return random.randint(0,500)
    else:
        return random.randint(1500,max)