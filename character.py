"""
THIS FILE STORES ALL CHARACTER CLASSES
"""

import pygame,mkrpg
pygame.init()

# MAIN CHARACTER (A DOCTOR)
class User(pygame.sprite.Sprite):
    def __init__(self,screen):
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/characters/user/01east.bmp")
        self.image = self.image.convert()
        tranColor = self.image.get_at((1,1))
        self.image.set_colorkey(tranColor)
        self.rect = self.image.get_rect()
        self.x = 320
        self.y = 385
        self.rect.center = (self.x,self.y)
        self.dir = 0
        self.speed = 5
        self.hitPoints = 25
        self.hitPointsMax = 25
        self.attackSkill = 5
        self.lives = 3
        self.xp = 0
    def reset(self):
        self.x = 320
        self.y = 385
        self.rect.center = (self.x, self.y)
        self.hitPoints = self.hitPointsMax
    def update(self):
        self.checkKeys()
        self.updateImage(dir)
        self.checkBounds()
        self.rect.center = (self.x, self.y)
    def checkKeys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.dir = 180
            self.x += (-1 * self.speed)
        if keys[pygame.K_RIGHT]:
            self.dir = 0
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.dir = 90
            self.y += (-1 * self.speed)
        if keys[pygame.K_DOWN]:
            self.dir = 270
            self.y += self.speed
    def updateImage(self,dir):
        if self.dir == 0:
            self.image = pygame.image.load("images/characters/user/01east.bmp")
            self.image = self.image.convert()
            tranColor = self.image.get_at((1,1))
            self.image.set_colorkey(tranColor)
            self.rect = self.image.get_rect()
        if self.dir == 90:
            self.image = pygame.image.load("images/characters/user/01north.bmp")
            self.image = self.image.convert()
            tranColor = self.image.get_at((1,1))
            self.image.set_colorkey(tranColor)
            self.rect = self.image.get_rect()
        if self.dir == 180:
            self.image = pygame.image.load("images/characters/user/01west.bmp")
            self.image = self.image.convert()
            tranColor = self.image.get_at((1,1))
            self.image.set_colorkey(tranColor)
            self.rect = self.image.get_rect()
        if self.dir == 270:
            self.image = pygame.image.load("images/characters/user/01south.bmp")
            self.image = self.image.convert()
            tranColor = self.image.get_at((1,1))
            self.image.set_colorkey(tranColor)
            self.rect = self.image.get_rect()
    def checkBounds(self):
        scrWidth = self.screen.get_width()
        scrHeight = 385
        if self.x >= scrWidth:
            self.x = 640
        if self.x <= 150:
            self.x = 150
        if self.y >= scrHeight:
            self.y = 385
        if self.y <= 0:
            self.y = 0
    def stop(self):
        self.speed = 0
    def start(self):
        self.speed = 5
    def death(self):
        pygame.quit()

# A MENTALLY ILL WOMAN
class MentallyIllWoman(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load("images/characters/girl/stopped0000.bmp")
        self.image = self.image.convert()
        tranColor = self.image.get_at((1,1))
        self.image.set_colorkey(tranColor)
        self.rect = self.image.get_rect()
        self.x = 320
        self.y = 40
        self.rect.center = (self.x, self.y)
        self.dir = 0
        self.speed = 0
        self.hitPoints = 28
        self.attackSkill = 6
        self.xp = 25
    def death(self):
        self.speed = 0
        self.x = -200
        self.y = -200
        self.rect.center = (self.x, self.y)
    def reset(self):
        self.x = 320
        self.y = 40
        self.rect.center = (self.x, self.y)
        self.hitPoints = 28

# MENTALLY ILL WOMAN'S DRUNK HUSBAND
class DrunkHusband(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load("images/characters/farmer/stopped0006.bmp")
        self.image = self.image.convert()
        tranColor = self.image.get_at((1,1))
        self.image.set_colorkey(tranColor)
        self.rect = self.image.get_rect()
        self.x = 150
        self.y = 40
        self.rect.center = (self.x,self.y)
        self.dir = 0
        self.speed = 0
        self.hitPoints = 10
        self.attackSkill = 2
        self.xp = 3
    def death(self):
        self.speed = 0
        self.x = -200
        self.y = -200
        self.rect.center = (self.x, self.y)
    def reset(self):
        self.x = 60
        self.y = 40
        self.rect.center = (self.x, self.y)
        self.hitPoints = 10

# CORPSE LADY
class CorpseLady(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load("images/characters/corpse/01east.bmp")
        self.image = self.image.convert()
        tranColor = self.image.get_at((1,1))
        self.image.set_colorkey(tranColor)
        self.rect = self.image.get_rect()
        self.x = 320
        self.y = 240
        self.rect.center = (self.x,self.y)
        self.dir = 0
        self.speed = 5
        self.hitPoints = 30
        self.attackSkill = 3
        self.xp = 15
    def update(self):
        self.x += self.speed 
        self.updateImage(dir)
        self.checkBounds() 
        self.rect.center = (self.x, self.y)
    def updateImage(self,dir):
        if self.dir == 0:
            self.image = pygame.image.load("images/characters/corpse/01east.bmp")
            self.image = self.image.convert()
            tranColor = self.image.get_at((1,1))
            self.image.set_colorkey(tranColor)
            self.rect = self.image.get_rect()
        else:
            self.image = pygame.image.load("images/characters/corpse/01west.bmp")
            self.image = self.image.convert()
            tranColor = self.image.get_at((1,1))
            self.image.set_colorkey(tranColor)
            self.rect = self.image.get_rect()
    def checkBounds(self):
        scrWidth = self.screen.get_width()
        if self.x >= scrWidth:
            self.dir += 180
            self.speed *= -1
        elif self.x <= 150:
            self.dir -= 180
            self.speed *= -1
    def stop(self):
        self.speed = 0
    def start(self):
        self.speed = 5
    def death(self):
        self.speed = 0
        self.x = -200
        self.y = -200
        self.rect.center = (self.x, self.y)
    def reset(self):
        self.x = 320
        self.y = 240
        self.rect.center = (self.x, self.y)
        self.hitPoints = 30

# MUSHROOM MAN
class Mushroom(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load("images/characters/mushy/mush.bmp")
        self.image = self.image.convert()
        tranColor = self.image.get_at((1,1))
        self.image.set_colorkey(tranColor)
        self.rect = self.image.get_rect()
        self.x = 300
        self.y = 240
        self.rect.center = (self.x,self.y)
        self.dir = 0
        self.speed = 0
        self.hitPoints = 15
        self.attackSkill = 4
        self.xp = 3
    def death(self):
        self.hitPoints = 0
    def reset(self):
        self.x = 60
        self.y = 40
        self.rect.center = (self.x, self.y)
        self.hitPoints = 15
