import pygame as pg
import tkinter #python 3 syntax

root = tkinter.Tk()
root.withdraw()

WIDTH, HEIGHT = root.winfo_screenwidth(), root.winfo_screenheight()


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
GRIDWIDTH = int(round(WIDTH / TILESIZE))
GRIDHEIGHT = int(round(HEIGHT / TILESIZE))



PLAYERANIMATION = []
playeranimationraw = ["player0.png","player1.png","player2.png","player3.png","player4.png","player5.png","player6.png","player7.png"]
for i in range(8):
    PLAYERANIMATION.append(pg.transform.scale(pg.image.load(playeranimationraw[i]), (96, 96)))

MAPTILES = []
maptilesraw = ["floor.png","floor2.png","wall.png","sofa.png"]
for a in range(4):
    MAPTILES.append(pg.transform.scale(pg.image.load(maptilesraw[a]), (TILESIZE, TILESIZE)))