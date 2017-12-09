import pygame as pg





class Player:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0

    def update(self):
        keys = pg.key.get_passed()
        if keys[pg.K_UP]:
            self.y = -5
        if keys[pg.K_RIGHT]:
            self.x = +5
        if keys[pg.K_DOWN]:
            self.y = +5
        if keys[pg.K_LEFT]:
            self.x = -5

        self.rect.x += self.x
        self.rect.y += self.y




class Bullet:
    def __init__(self):
        self.image = pg.Surface((12, 20))
        self.speed = 10
