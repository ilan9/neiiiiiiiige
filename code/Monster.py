import pygame

class Monster(pygame.sprite.Sprite) :
    def __init__(self,x,y,list_wall):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.velocity = 4
        
        image = self.image = pygame.image.load('asset/zombie.png') #L'image de nos monstres
        
        #La taille du monstre :
        self.image_height = 84/1.5
        self.image_width = 72/1.5
        self.image = pygame.transform.scale(image, (self.image_width, self.image_height)) 
        
        #Son ID_BoX ///////////
        self.rect = self.image.get_rect()
        
        #La position de départ de notre monstre :
        self.rect.x = x
        self.rect.y = y

        self.list_wall = list_wall