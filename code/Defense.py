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
        self.image = pygame.image.load("asset/canon.png")
        self.rect = self.image.get_rect()
        
        self.image = pygame.transform.scale(self.image, (200, 200))
        
        self.rect.x = x
        self.rect.y = y
    