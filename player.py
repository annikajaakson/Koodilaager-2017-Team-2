import pygame as pg
from settings import *


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

    def move(self):
        key = pg.key.get_pressed()

        self.y += MOVE * key[pg.K_DOWN] - MOVE * key[pg.K_UP]
        self.x += MOVE * key[pg.K_RIGHT] - MOVE * key[pg.K_LEFT]

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y



