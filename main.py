import pygame as pg
import sys
from player import *
from map import *
from NPC import *
from settings import *

class Game:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

    def load_data(self):
        pass

    def new(self):
        self.allsprites = pg.sprite.Group()
        self.player = Player(self,10,10)

    def run(self):
        self.playing = True

        while self.playing:
            self.dt = self.clock.tick(FPS)/1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0,WIDTH,TILESIZE):
            pg.draw.line(self.screen,LIGHTGREY,(x,0),(x,HEIGHT))

        for y in range(0,HEIGHT,TILESIZE):
            pg.draw.line(self.screen,LIGHTGREY,(0,y),(WIDTH,y))

    def draw(self):
        self.screen_fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.map = Map.map_data

        for i in self.map:
            for a in i:
                if a == 0:
                    self.image = pg.Surface((TILESIZE, TILESIZE))
                    self.image.fill(BLACK)
                    self.rect = self.image.get_rect()
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)

g = Game()

while True:
    g.new()
    g.run()
