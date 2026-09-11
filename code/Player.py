import pygame

class Player(pygame.sprite.Sprite) :
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.velocity = 1
        
        image = self.image = pygame.image.load('asset/ranais.png') #L'image de notre joueur
        
        #La taille du joueur :
        self.image_height = 75
        self.image_width = 100
        self.image = pygame.transform.scale(image, (self.image_width, self.image_height)) 
        
        #Son ID_BoX ///////////
        self.rect = self.image.get_rect()
        
        #La position de départ de notre joueur :
        self.rect.x = 50 
        self.rect.y = 50

        # On peut l'enlever ??
    """   
    def update(self) :
        key = pygame.key.get_pressed()
        
        if key[pygame.K_LEFT] and self.rect.x > 0 : ############ METTRE EN PARAM7TRE PLUTOT
            self.rect.x -= self.velocity
            
        if key[pygame.K_RIGHT] and self.rect.x < 800 - self.image_width :############ METTRE EN PARAM7TRE PLUTOT
            self.rect.x += self.velocity
            
        if key[pygame.K_DOWN] and self.rect.y < 600 - self.image_height :############ METTRE EN PARAM7TRE PLUTOT
            self.rect.y += self.velocity
            
        if key[pygame.K_UP] and self.rect.y > 0 :############ METTRE EN PARAM7TRE PLUTOT
            self.rect.y -= self.velocity 
    """      
    def update(self) :
        key = pygame.key.get_pressed()
        velocity_x = 0
        velocity_y = 0
            
        if key[pygame.K_LEFT] and self.rect.x > 0 : ############ METTRE EN PARAM7TRE PLUTOT
            velocity_x -= self.velocity
                
        if key[pygame.K_RIGHT] and self.rect.x < 800 - self.image_width :############ METTRE EN PARAM7TRE PLUTOT
            velocity_x += self.velocity
                
        if key[pygame.K_DOWN] and self.rect.y < 600 - self.image_height :############ METTRE EN PARAM7TRE PLUTOT
            velocity_y += self.velocity
                
        if key[pygame.K_UP] and self.rect.y > 0 :############ METTRE EN PARAM7TRE PLUTOT
            velocity_y -= self.velocity 

        if velocity_x != 0 and velocity_y != 0:
            self.rect.x += velocity_x * 0.707 #Pour que les déplacement soit moins rapide en diagonnal
            self.rect.y += velocity_y * 0.707
        else:
            self.rect.x += velocity_x
            self.rect.y += velocity_y

        
        