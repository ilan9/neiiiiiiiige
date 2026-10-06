import pygame

class Defense(pygame.sprite.Sprite): # Elle doit hérite de sprite.Sprite car on veut les mettre dans un groupe
    def __init__(self, x, y, health) :
        super().__init__()
        self.life = health ## Une vie ??
        self.max_life = health
       
       
    def hurt(self, damage):
        self.life -= damage
        if self.life < 0 :
            self.kill()
            
class Canon(Defense) :
    def __init__(self, x, y, health):
        super().__init__(x, y, health)
        self.images = [
            pygame.transform.scale(pygame.image.load("asset/canon_animation/canon1.png"), (200,200)),
            pygame.transform.scale(pygame.image.load("asset/canon_animation/canon2.png"), (200,200)),
            pygame.transform.scale(pygame.image.load("asset/canon_animation/canon3.png"), (200,200)),
            pygame.transform.scale(pygame.image.load("asset/canon_animation/canon4.png"), (200,200)),
            pygame.transform.scale(pygame.image.load("asset/canon_animation/canon5.png"), (200,200)),
            pygame.transform.scale(pygame.image.load("asset/canon_animation/canon6.png"), (200,200))
        ]
        
        self.current_frame = 0
        
        self.image = self.images[self.current_frame]        
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        
        self.is_animating = False
        self.last_time_anime = 0
        self.animation_speed = 500
        
    def update(self):
        nb_images = len(self.images)
        if self.is_animating :
            current_time = pygame.time.get_ticks()
            
            if self.last_time_anime + self.animation_speed/nb_images <= current_time :
                self.current_frame = self.current_frame + 1
                self.last_time_anime = pygame.time.get_ticks()
                
                if self.current_frame >= nb_images :
                    self.current_frame = 0
                    self.is_animating = False
                
                self.image = self.images[self.current_frame]
    
    def tirer(self) :
        self.is_animating = True
        self.last_time_anime = pygame.time.get_ticks()
    
class Projectiles() :
    def __init__(self, x, y) :
        self.image = pygame.image.load("")
        
        self.velocity = 10
        self.damage = 10 