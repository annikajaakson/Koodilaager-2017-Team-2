import pygame
from NPC import*
from player import*


class Bullet:
    def __init__(self, x, y, player):
        self.bullet_speed = 500
        self.bullet_lifetime = 50
        self.rect = pygame.Rect([self.x, self.y, 1, 1])
        self.x = player.x
        self.y = player.y

    def bullet_kill(self, opilane):
        if opilane.x == self.x and opilane.y == self.y:
            self.bullet_lifetime = 0
