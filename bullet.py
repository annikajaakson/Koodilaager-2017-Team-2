import pygame, math
from NPC import*
from random import randint
#from player import*


class Bullet:
    def __init__(self, x, y, suund):
        self.bullet_speed = 500
        self.bullet_lifetime = 50
        #self.icon = pygame.image.load("bullet.png")
        self.x = x
        self.y = y
        #self.rect = pygame.Rect([self.x, self.y, 3, 3])
        self.suund = suund - 90
        if self.suund < 0:
            self.suund += 360
        self.speed = 15
        self.color = [randint(200, 255), randint(0, 25), randint(223, 255)]

    def bullet_kill(self, opilane):
        if opilane.x == self.x and opilane.y == self.y:
            self.bullet_lifetime = 0

    def update(self, bulletlist):
        self.x += self.speed * math.cos(self.suund*math.pi/180)
        self.y -= self.speed * math.sin(self.suund*math.pi/180)

        if self.x < 0 or self.x > WIDTH or self.y < 0 or self.y > HEIGHT:
            bulletlist.remove(self)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, 10, 10])