import ctypes
import pygame as pg
user32 = ctypes.windll.user32
WIDTH, HEIGHT = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

FPS = 60
MOVE = 5
PLAYERMOVE = 5
TITLE = "Koolitulistamine"
BGCOLOR = BLACK


TILEAMOUNTY = 32
TILESIZE = int(round(HEIGHT/TILEAMOUNTY))
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE


PLAYERANIMATION = []
playeranimationraw = ["player0.png","player1.png","player2.png","player3.png","player4.png","player5.png","player6.png","player7.png"]
for i in range(8):
    PLAYERANIMATION.append(pg.transform.scale(pg.image.load(playeranimationraw[i]), (96, 96)))