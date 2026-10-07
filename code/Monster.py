import pygame
from Outils import decoup_image

class Monster(pygame.sprite.Sprite) :
    def __init__(self,x,y,group_wall,home, group_rampart ):
        super().__init__()
        self.health = 10
        self.max_health = 10
        self.last_time_hit = 0 #la dernière fois que le monstre a attaqué pour la gestion des coups.
        self.velocity = 0.6
        self.damage = 1
        self.cooldown = 1000 #1s entre chaque coup 
        
        image = self.image = pygame.image.load('asset/zombie.png') #L'image de nos monstres

        #Animations
        self.anim = {"walk":decoup_image("asset/zombie_animation/Zombie_Default_Walk.png",384,64,6,1),
                     "attack":decoup_image("asset/zombie_animation/Zombie_Default_Attack.png",384,64,6,1),
                     "hurt":decoup_image("asset/zombie_animation/Zombie_Default_Hurt.png",384,64,6,1),
                     "dead":decoup_image("asset/zombie_animation/Zombie_Default_Dead.png",384,64,6,1)
                     }
        self.image = self.anim["walk"][0]
        
        #La taille du monstre :
        self.image_height = 64 * 1.5
        self.image_width = 384/6 * 1.5
        self.image = pygame.transform.scale(self.image, (self.image_width, self.image_height))
        self.anim_time = 1000/6
        self.anim_type = "walk"
        
        #Son ID_BoX ///////////
        self.rect = self.image.get_rect()

        self.group_wall = group_wall
        self.home = home # l'objectif du monstre
        self.group_rampart = group_rampart
        
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
        last_posx = self.rect.x
        last_posy = self.rect.y

        self.posfin_x += self.motion_x * self.velocity #On crée ces variable temporaire car rect 
        self.posfin_y += self.motion_y * self.velocity # ne peut pas prendre de float et ca creerai un décalage
        self.rect.x = self.posfin_x
        self.rect.y = self.posfin_y
        self.anim_type = "walk"


        rampart = pygame.sprite.spritecollideany(self,self.group_rampart)# SI il est dans un mur_destructible on l'attaque
        if rampart:
            self.attack(rampart)
            

        if pygame.sprite.spritecollideany(self,self.group_wall):# SI il est dans un mur on le replace a sa position précédente
            self.rect.x = last_posx
            self.rect.y = last_posy
            self.posfin_x = self.rect.x
            self.posfin_y = self.rect.y


        if pygame.sprite.collide_rect(self,self.home):
            if self.home.life > 0:
                self.attack(self.home)
    

            
    def hurt(self, damage):
        # Se blesse lui
        actual_time = pygame.time.get_ticks()
        
        # On subit des dégats à chaque cooldown.
        #if actual_time - self.last_time_hit > cooldown :
        self.health -= damage
           #self.last_time_hit = actual_time
    
    def attack(self, element):
        actual_time = pygame.time.get_ticks()
        

        if actual_time - self.last_time_hit > self.cooldown :
            element.hurt(self.damage)
            print(element.life)
            self.last_time_hit = actual_time
            #si il attaque il peut aussi "glisser le long du mur donc on recalcule la direction jusqu'à la maison"
            self.motion_x,self.motion_y = self.motion_calcul()