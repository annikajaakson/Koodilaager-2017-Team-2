import pygame as pg
from settings import *
from math import *
from bullet import *


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
        self.counter = PLAYERMOVE
        self.playernumber = 0
        self.suund = 0

    def move(self, bulletlist):
        key = pg.key.get_pressed()

        if key[pg.K_SPACE]:
            if self.cooldown == 0:
                bulletlist.append(Bullet(self.x, self.y, self.suund))
                self.cooldown += 1
        elif key[pg.K_SPACE] == 0:
            self.cooldown = 0

        ver = MOVE * key[pg.K_DOWN] - MOVE * key[pg.K_UP]
        hor = MOVE * key[pg.K_RIGHT] - MOVE * key[pg.K_LEFT]
        self.a = 1
        if hor == MOVE:
            self.suund = 90
            if ver == MOVE:
                self.suund = 45
            elif ver == -MOVE:
                self.suund = 135
        elif hor == -MOVE:
            self.suund = 270
            if ver == MOVE:
                self.suund = 315
            elif ver == -MOVE:
                self.suund = 225
        else:
            if ver == MOVE:
                self.suund = 0
            elif ver == -MOVE:
                self.suund = 180
        if abs(ver)+abs(hor) == MOVE*2:
            self.y += ver/sqrt(2)
            self.x += hor/sqrt(2)
        else:
            self.y += ver
            self.x += hor
        if ver == 0 and hor == 0:#et kohapeal jalad ei liiguks
            self.a = 0

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self,screen):
        self.counter -= 1
        if self.counter == 0:
            self.playernumber += 1
            if self.playernumber == 8:
                self.playernumber = 0
            self.counter = PLAYERMOVE

        if self.x > 1920-96+8:
            self.x = 1920-96+8
        if self.x < 0-8:
            self.x = 0-8
        if self.y > 1080-96+8:
            self.y = 1080-96+8
        if self.y < 0-8:
            self.y = 0-8

        if self.a == 0:
            image = PLAYERANIMATION[0]
        else:
            image = PLAYERANIMATION[self.playernumber]
        img_rect = image.get_rect()
        rot_image = pg.transform.rotate(image,self.suund)
        rot_im_rect = rot_image.get_rect()
        rot_im_rect.center = img_rect.center
        screen.blit(rot_image,(rot_im_rect[0]+self.x,rot_im_rect[1]+self.y))