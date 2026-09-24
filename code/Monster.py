import pygame

class Monster(pygame.sprite.Sprite) :
    def __init__(self,x,y,list_wall,home):
        super().__init__()
        self.health = 10
        self.max_health = 10
        self.last_time_hit = 0 #la dernière fois que le monstre a attaqué pour la gestion des coups.
        self.velocity = 0.6
        
        image = self.image = pygame.image.load('asset/zombie.png') #L'image de nos monstres
        
        #La taille du monstre :
        self.image_height = 84/1.5
        self.image_width = 72/1.5
        self.image = pygame.transform.scale(image, (self.image_width, self.image_height)) 
        
        #Son ID_BoX ///////////
        self.rect = self.image.get_rect()

        self.list_wall = list_wall
        self.home = home # l'objectif du monstre
        
        #La position de départ de notre monstre :
        self.rect.x = x
        self.rect.y = y
        self.motion_x,self.motion_y = self.motion_calcul()
        self.posfin_x = x # Pour le calcul du mouvement car rect ne peut stocker que des int 
        self.posfin_y = y

        

    def motion_calcul(self):# Calcul du mouvement du monstre 1 seul fois 
        posstart_x = self.rect.x
        posstart_y = self.rect.y
        posfin_x = self.home.rect.x
        posfin_y = self.home.rect.y

        distance_x = posfin_x - posstart_x
        distance_y = posfin_y - posstart_y
        distance_norm = (distance_x**2 + distance_y**2) ** 0.5 # pythagore
        return distance_x/distance_norm,distance_y/distance_norm




    def update(self):
        self.posfin_x += self.motion_x * self.velocity #On crée ces variable temporaire car rect 
        self.posfin_y += self.motion_y * self.velocity # ne peut pas prendre de float et ca creerai un décalage
        self.rect.x = self.posfin_x
        self.rect.y = self.posfin_y 

        if pygame.Rect.colliderect(self.rect,self.home.rect):
            self.home.hurt(1)
            self.kill()
            
            
    def hurt(self, damage):
        temps_actuel = pygame.time.get_ticks()
    
        cooldown = 1000 #1s entre chaque coup ????
        
        # On inflige des dégats à chaque cooldown.
        #if temps_actuel - self.last_time_hit > cooldown :
        self.health -= damage
           #self.last_time_hit = temps_actuel