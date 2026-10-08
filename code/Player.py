import pygame

class Player(pygame.sprite.Sprite) :
    def __init__(self,x,y,border_x,border_y,list_wall, group_monster):
        super().__init__()
        self.health = 500
        self.max_health = 500
        self.last_time_hit = 0 #la dernière fois que le joueur a attaqué pour la gestion des coups.
        self.cooldown = 1000
        self.velocity = 4
        self.damage = 5

        self.monster_atq = {}
        
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

        self.group_monster = group_monster
        self.list_wall = list_wall


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
        if pygame.sprite.spritecollideany(self,self.list_wall):
            self.rect.x = last_posx
            self.rect.y = last_posy

        # Attaquer les monstres
        self.attack_monster()
            
    def attack_monster(self):
        colliding_monsters = pygame.sprite.spritecollide(self, self.group_monster, False)
        for monster in colliding_monsters :
            #On attaque le monstre qu'une fois par seconde
            if monster in self.monster_atq:
                if pygame.time.get_ticks() - self.monster_atq[monster] > self.cooldown:
                    self.monster_atq.pop(monster)
            else:
                monster.hurt(self.damage)
                self.hurt(5) # Le joueur prends des dégats si il attaque le monstre
                self.monster_atq[monster] = pygame.time.get_ticks()
                print("attq subie") 


    def attack_1_persecond(self, element): # PAs utilisé pour l'instant
        actual_time = pygame.time.get_ticks()
        if actual_time - self.last_time_hit > self.cooldown :
            element.hurt(self.damage)
            self.last_time_hit = actual_time
        
    def hurt(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.dead()
    
    def dead(self):
        print("Le joueur est mort !!!")
        # Respawn dans 30 sec ??