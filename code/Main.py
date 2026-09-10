import pygame
import pytmx #pour lire Tiled

from Time import Time

# Gestion de fenetre pygame
pygame.init()
fenetre = pygame.display.set_mode((800, 600))
pygame.display.set_caption("hiver")

tmx_data = pytmx.util_pygame.load_pygame("Tiled/test_carte.tmx") # charger la carte

# Initialiser les éléments
time = Time()
calque_nuit = pygame.Surface((800,600))
calque_nuit.fill((0,0,30))

# Fenetre pygame reste ouverte
quit = False
while not quit: #Pour garder la fenetre ouverte
    for event in pygame.event.get(): #Ecouter les évenements "uniques"
        if event.type == pygame.QUIT:
            quit = True
            # Pour quitter proprement
        elif event.type == pygame.KEYDOWN: # Detecter TOUTES les touches pressées
            if event.key == pygame.K_p:
                time.changer_phase() # Cf: Time.py


    # Mise à jour des éléments
    time.update()
    calque_nuit.set_alpha(time.opacite)


    # Afficher la carte
    for layer in tmx_data.visible_layers: #C'est les couches dans Tiled
        if isinstance(layer,pytmx.TiledTileLayer): #On vérifie que c'est des layer et pas des objets et que ils sont en mode visible
            for x,y,image in layer.tiles(): # On recup les coordonnées et les image de chaque tuile
                pos_x = x*tmx_data.tilewidth 
                # On multiplie leur position par leur largeur 
                pos_y = y*tmx_data.tileheight
                fenetre.blit(image,(pos_x,pos_y)) # On les affiche dans notre fenetre

    # Dessiner la surcouche
    fenetre.blit(calque_nuit,(0,0)) # le calque de nuit
    
    police = pygame.font.Font(None, 30) #Police par default taille 30
    ecrit_phase = police.render("Phase ("+str(time.phase)+"): "+str(time.jour_etat), True, (0, 0, 0)) #Ecrit mon texte avec la couleur 0,0,0
    fenetre.blit(ecrit_phase, (330,10)) #Dessine mon texte à la position 330,10
    
    pygame.display.flip() # Met a jour l'écran

pygame.quit() # fermer la fenetre pygame