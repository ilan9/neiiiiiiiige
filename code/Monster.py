import pygame

class Monster(pygame.sprite.Sprite) :
    def __init__(self,x,y,list_wall,home:pygame.Rect):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.velocity = 2
        
        image = self.image = pygame.image.load('asset/zombie.png') #L'image de nos monstres
        
        #La taille du monstre :
        self.image_height = 84/1.5
        self.image_width = 72/1.5
        self.image = pygame.transform.scale(image, (self.image_width, self.image_height)) 
        
        #Son ID_BoX ///////////
        self.rect = self.image.get_rect()

        self.list_wall = list_wall
        self.home:pygame.Rect = home # l'objectif du monstre
        
        #La position de départ de notre monstre :
        self.rect.x = x
        self.rect.y = y
        self.motion_x,self.motion_y = self.motion_calcul()
        self.posfin_x = x # Pour le calcul du mouvement car rect ne peut stocker que des int 
        self.posfin_y = y

        

    def motion_calcul(self):# Calcul du mouvement du monstre 1 seul fois 
        posstart_x = self.rect.x
        posstart_y = self.rect.y
        posfin_x = self.home.x
        posfin_y = self.home.y

        distance_x = posfin_x - posstart_x
        distance_y = posfin_y - posstart_y
        distance_norm = (distance_x**2 + distance_y**2) ** 0.5 # pythagore
        return distance_x/distance_norm,distance_y/distance_norm




    def update(self):
        posfin_x = self.posfin_x + self.motion_x * self.velocity
        posfin_y = self.posfin_y + self.motion_y * self.velocity
        self.rect.x += posfin_x/200
        self.rect.y += posfin_y/200 # Sinon il vas beaucoup trop vite

        if pygame.Rect.colliderect(self.rect,self.home):
            print("monstre a touché la maison")
            self.rect.x = 10000 #Temporaire plus tard le faire attaquer ou le détruire