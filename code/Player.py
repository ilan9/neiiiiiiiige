import pygame

class Player(pygame.sprite.Sprite) :
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.velocity = 4
        
        image = self.image = pygame.image.load('asset/ranais.png') #L'image de notre joueur
        
        #La taille du joueur :
        self.image = pygame.transform.scale(image, (250, 200)) 
        
        #Son ID_BoX ///////////
        self.rect = self.image.get_rect()
        
        #La position de départ de notre joueur :
        self.rect.x = 50 
        self.rect.y = 50
        
    def update(self) :
        key = pygame.key.get_pressed()
        
        if key[pygame.K_LEFT] and self.rect.x > 0 : ############ METTRE EN PARAM7TRE PLUTOT
            self.rect.x -= self.velocity
            
        if key[pygame.K_RIGHT] and self.rect.x < 600 :############ METTRE EN PARAM7TRE PLUTOT
            self.rect.x += self.velocity
            
        if key[pygame.K_DOWN] and self.rect.y < 400 :############ METTRE EN PARAM7TRE PLUTOT
            self.rect.y += self.velocity
            
        if key[pygame.K_UP] and self.rect.y > 0 :############ METTRE EN PARAM7TRE PLUTOT
            self.rect.y -= self.velocity 
            
        
        