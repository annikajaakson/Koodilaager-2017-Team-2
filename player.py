import pygame as pg
from settings import *
from math import *


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.counter = 15
        self.playernumber = 0
        self.suund = 0

    def move(self):
        key = pg.key.get_pressed()

        ver = MOVE * key[pg.K_DOWN] - MOVE * key[pg.K_UP]
        hor = MOVE * key[pg.K_RIGHT] - MOVE * key[pg.K_LEFT]
        if ver == MOVE:
            self.suund = 0
            if hor == MOVE:
                self.suund = 0
            elif hor == -MOVE:
                self.suund = 0
        if ver == -MOVE:
            self.suund = 180
            if hor == MOVE:
                self.suund = 0
            elif hor == -MOVE:
                self.suund = 0
        if hor == MOVE:
            self.suund = 90
            if ver == MOVE:
                self.suund = 0
            elif ver == -MOVE:
                self.suund = 0
        if hor == -MOVE:
            self.suund = 270
            if ver == MOVE:
                self.suund = 0
            elif ver == -MOVE:
                self.suund = 0
        if abs(ver)+abs(hor) == MOVE*2:
            self.y += ver/sqrt(2)
            self.x += hor/sqrt(2)
        else:
            self.y += ver
            self.x += hor


    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self,screen):
        self.counter -= 1
        if self.counter == 0:
            self.playernumber += 1
            if self.playernumber == 8:
                self.playernumber = 0
            self.counter = 15
        rotated = pg.transform.rotate(PLAYERANIMATION[self.playernumber],self.suund)
        screen.blit(rotated, (self.x, self.y))