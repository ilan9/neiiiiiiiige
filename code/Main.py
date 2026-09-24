import pygame
import pytmx #pour lire Tiled

from Time import Time
from Player import Player
from Camera import Camera
from Home import Home
from Monster import Monster
from Spawner import monster_spawner



# Gestion de window pygame
pygame.init()
window_width, window_height = 800,600 
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("hiver")

pygame.time.Clock().tick(60) # limiter a 60 fps


tmx_data = pytmx.util_pygame.load_pygame("Tiled/test_carte.tmx") # charger la carte
map_width = tmx_data.width*tmx_data.tilewidth
map_height = tmx_data.width*tmx_data.tilewidth

list_wall = []

# Recuperer les objets sur la carte Tiled
for layer in tmx_data.objects:
    if layer.type == "Wall":
        list_wall.append(pygame.Rect(layer.x,layer.y,layer.width,layer.height))
    if layer.type == "Home":
        home = Home(pygame.Rect(layer.x,layer.y,layer.width,layer.height))

# Initialiser les éléments
time = Time()
layer_night = pygame.Surface((window_width, window_height))
layer_night.fill((0,0,30))

player = Player(50,50,map_width,map_height,list_wall) # charge le joueur
camera = Camera(map_width,map_height,window_width, window_height) # charge la camera
group_monster = pygame.sprite.Group()# Comme une liste mais les methode de monstre s'utilise direct sur group (voir update)


# window pygame reste ouverte
quit = False
while not quit: #Pour garder la window ouverte
    for event in pygame.event.get(): #Ecouter les évenements "uniques"
        if event.type == pygame.QUIT:
            quit = True
            # Pour quitter proprement
        elif event.type == pygame.KEYDOWN: # Detecter TOUTES les touches pressées
            if event.key == pygame.K_p: # Changer de phase
                time.change_phase() # Cf: Time.py
            elif event.key == pygame.K_m: # Faire apparaitre un monstre
                monster_spawner(group_monster,map_width,map_height,list_wall,home)

    
    
    # Mise à jour des éléments
    player.update()
    time.update()
    layer_night.set_alpha(time.opacity)
    camera.update(player)
    group_monster.update() # Update tous les monstre du groupe
    
    #Potentiels dégats :
    colliding_monsters = pygame.sprite.spritecollide(player, group_monster, False)
    for monsters in colliding_monsters :
        monsters.hurt(10)
        if monsters.health < 0 :
            monsters.kill()
        
        player.hurt(5)
        if player.health < 0 :
            player.kill()

    # Afficher la carte
    for layer in tmx_data.visible_layers: #C'est les couches dans Tiled
        if isinstance(layer,pytmx.TiledTileLayer): #On vérifie que c'est des layer et pas des objets et que ils sont en mode visible
            for x,y,image in layer.tiles(): # On recup les coordonnées et les image de chaque tuile
                pos_x = x*tmx_data.tilewidth 
                # On multiplie leur position par leur largeur 
                pos_y = y*tmx_data.tileheight
                window.blit(image,camera.apply(pos_x,pos_y)) # On les affiche dans notre window

    # Dessiner la surcouche
    window.blit(layer_night,(0,0)) # le opacite de nuit
    window.blit(player.image, camera.apply(player.rect.x,player.rect.y))
    for monster in group_monster.sprites(): # Dessiner les monstres
        window.blit(monster.image,camera.apply(monster.rect.x,monster.rect.y))
    
    police = pygame.font.Font(None, 30) #Police par default taille 30
    text_phase = police.render("Phase ("+str(time.phase)+"): "+str(time.day_etat), True, (0, 0, 0)) #Ecrit mon texte avec la couleur 0,0,0
    window.blit(text_phase, (330,10)) #Dessine mon texte à la position 330,10

    pv_home = police.render("Maison PV : "+str(home.life), True, (0, 0, 0)) # PV de la maison
    window.blit(pv_home, (5,10))
    
    pv_joueur = police.render("Joueur PV : "+str(player.health), True, (0, 0, 0)) # PV de la maison
    window.blit(pv_joueur, (600,10))
    
    pygame.display.flip() # Met a jour l'écran

pygame.quit() # fermer la window pygame
