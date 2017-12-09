import pygame as pg
import sys
from player import *
from map import *
from NPC import *
from settings import *

class Game:

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((0,0),FULLSCREEN)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(1,1)
        self.load_data()
        self.opilased = []

    def load_data(self):
        pass

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.player = Player(self,10,10)

    def run(self):
        self.playing = True

        for i in range(ohvreidKokku):  # generate n cells
            Opilane = opilane()
            self.opilased.append(Opilane)

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
        self.player.move()

    def draw_grid(self):
        for x in range(0,WIDTH,TILESIZE):
            pg.draw.line(self.screen,LIGHTGREY,(x,0),(x,HEIGHT))

        for y in range(0,HEIGHT,TILESIZE):
            pg.draw.line(self.screen,LIGHTGREY,(0,y),(WIDTH,y))

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.map = Map()
        data = self.map.map_data
        self.all_sprites.draw(self.screen)

        for i in data:
            for a in i:
                if a == 0:
                    self.image = pg.Surface((TILESIZE, TILESIZE))
                    self.image.fill(BLACK)
                    self.rect = self.image.get_rect()

        for i in self.opilased: #update all cells
            i.wander()
            i.jookseb(self.player)
            i.draw()

        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                pass

g = Game()

while True:
    g.new()
    g.run()
