import pygame as pg
import sys
from player import *
from map import *
from NPC import *
from settings import *

class Game:

    def __init__(self):
        pg.init()
        self.FONT = pg.font.SysFont("monospace", 100)
        self.screen = pg.display.set_mode((0,0))
        self.window = (1920,1080)
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(1,1)
        self.load_data()
        self.opilased = []
        self.bullets = []

        map = Map()
        data = map.map()
        def joonista():
            for i in range(len(data)):
                for a in range(len(data[i])):
                    """
                    self.image = pg.Surface((TILESIZE, TILESIZE))
                    if data[i][a] == 0:
                        self.image.fill(GREEN)
                    elif data[i][a] == 1:
                        self.image.fill(YELLOW)

                    screen.blit(self.image,(TILESIZE*a,TILESIZE*i))
                    """
                    self.background.blit(MAPTILES[data[i][a]], (TILESIZE*a, TILESIZE*i))

        self.background = pg.Surface(self.window)
        joonista()


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
        self.player.move(self.bullets)
        for bullet in self.bullets:
            bullet.update(self.bullets)

    def draw_grid(self):
        for x in range(0,WIDTH,TILESIZE):
            pg.draw.line(self.screen,LIGHTGREY,(x,0),(x,HEIGHT))

        for y in range(0,HEIGHT,TILESIZE):
            pg.draw.line(self.screen,LIGHTGREY,(0,y),(WIDTH,y))

    def draw(self):
        self.screen.blit(self.background,(0,0))
        #self.draw_grid()

        #self.all_sprites.draw(self.screen)

        for i in self.opilased: #update all cells
            if i.alive:
                i.wander()
                i.jookseb(self.player)
                i.get_killed(self.bullets)
                i.draw(self.screen)
            else:
                self.background.blit(blood_img, (i.x, i.y))
                self.opilased.remove(i)

        self.screen.blit(self.FONT.render("fps: " + str(round(self.clock.get_fps())), 1, WHITE), (100, 100))
        self.player.draw(self.screen)
        for bullet in self.bullets:
            bullet.draw(self.screen)
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
