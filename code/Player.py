import pygame

class Player(pygame.sprite.Sprite) :
    def __init__(self,x,y,border_x,border_y,list_wall):
        super().__init__()
        self.health = 500
        self.max_health = 500
        self.last_time_hit = 0 #la dernière fois que le joueur a attaqué pour la gestion des coups.
        self.velocity = 4
        
        
        image = self.image = pygame.image.load('asset/ranais.png') #L'image de notre joueur
        
        #La taille du joueur :
        self.image_height = 75
        self.image_width = 100
        self.image = pygame.transform.scale(image, (self.image_width, self.image_height)) 
        
        #Son ID_BoX ///////////
        self.rect = self.image.get_rect()
        
        #La position de départ de notre joueur :
        self.rect.x = x
        self.rect.y = y
        self.border_x = border_x
        self.border_y = border_y

        self.list_wall = list_wall

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
        last_posx = self.rect.x
        last_posy = self.rect.y
            
        if key[pygame.K_LEFT] and self.rect.x > 0 : ############ METTRE EN PARAM7TRE PLUTOT
            velocity_x -= self.velocity
                
        if key[pygame.K_RIGHT] and self.rect.x < self.border_x - self.image_width :############ METTRE EN PARAM7TRE PLUTOT
            velocity_x += self.velocity
                
        if key[pygame.K_DOWN] and self.rect.y < self.border_y - self.image_height :############ METTRE EN PARAM7TRE PLUTOT
            velocity_y += self.velocity
                
        if key[pygame.K_UP] and self.rect.y > 0 :############ METTRE EN PARAM7TRE PLUTOT
            velocity_y -= self.velocity 

        if velocity_x != 0 and velocity_y != 0:
            self.rect.x += velocity_x * 0.707 #Pour que les déplacement soit moins rapide en diagonnal
            self.rect.y += velocity_y * 0.707
        else:
            self.rect.x += velocity_x
            self.rect.y += velocity_y
        #print((self.rect.x,self.rect.y))

        # test collision avec les murs, si ils se chevauche on annule le dernier mouv du joueur
        for wall in self.list_wall:
            if pygame.Rect.colliderect(wall,self):
                self.rect.x = last_posx
                self.rect.y = last_posy
        
    def hurt(self, damage):
        temps_actuel = pygame.time.get_ticks()
    
        cooldown = 1000 #1s entre chaque coup ????
        
        # On inflige des dégats à chaque cooldown.
        #if temps_actuel - self.last_time_hit > cooldown :
        self.health -= damage
            #self.last_time_hit = temps_actuel