import sys
import random
import pygame
from player import *
from bullet import *
from pygame.locals import *
from settings import *
pygame.init()


ohvreidKokku = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #set the game window

class opilane:
    def __init__(self):
        self.x = random.randrange(10, WIDTH-10) #x position
        self.y = random.randrange(10, HEIGHT-10) #y position
        self.speed = random.randrange(2, 3) #cell speed
        self.move = [None, None] #realtive x and y coordinates to move to
        self.direction = None #movement direction
        self.rect = pygame.Rect([self.x, self.y, TILESIZE, TILESIZE])


    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), self.rect) #draw the cell


    def opilanekill (self, bullet):
        if bullet.x == self.x and bullet.y == self.y:
            self.kill()

    def jookseb(self, player):
        if player.x > self.x:
            self.x -= 1
        elif player.x < self.x:
            self.x += 1
        if player.y > self.y:
            self.y -= 1
        elif player.y < self.y:
            self.y += 1

    def wander(self):
        directions = {"S":((-1,2),(1,self.speed)),"SW":((-self.speed,-1),(1,self.speed)),"W":((-self.speed,-1),(-1,2)),"NW":((-self.speed,-1),(-self.speed,-1)),"N":((-1,2),(-self.speed,-1)),"NE":((1,self.speed),(-self.speed,-1)),"E":((1,self.speed),(-1,2)),"SE":((1,self.speed),(1,self.speed))} #((min x, max x)(min y, max y))
        directionsName = ("S","SW","W","NW","N","NE","E","SE") #possible directions
        if random.randrange(0,5) == 2: #move about once every 5 frames
            if self.direction == None: #if no direction is set, set a random one
                self.direction = random.choice(directionsName)
            else:
                a = directionsName.index(self.direction) #get the index of direction in directions list
                b = random.randrange(a-1,a+2) #set the direction to be the same, or one next to the current direction
                if b > len(directionsName)-1: #if direction index is outside the list, move back to the start
                    b = 0
                self.direction = directionsName[b]
            smallOffset = random.random()  # Random floating-point number between 0 and 1 ("Tiny number")

            self.move[0] = random.randrange(directions[self.direction][0][0],
                                            directions[self.direction][0][1]) + smallOffset
            self.move[1] = random.randrange(directions[self.direction][1][0],
                                            directions[self.direction][1][1]) + smallOffset


        if self.x < 5 or self.x > WIDTH - 5 or self.y < 5 or self.y > HEIGHT - 5: #if cell is near the border of the screen, change direction
            if self.x < 5:
                self.direction = "E"
            elif self.x > WIDTH - 5:
                self.direction = "W"
            elif self.y < 5:
                self.direction = "S"
            elif self.y > HEIGHT - 5:
                self.direction = "N"
            self.move[0] = random.randrange(directions[self.direction][0][0],directions[self.direction][0][1]) #change relative x to a random number between min x and max x
            self.move[1] = random.randrange(directions[self.direction][1][0],directions[self.direction][1][1]) #change relative x to a random number between min x and max x

        if self.move[0] != None: #add the relative coordinates to the cells coordinates
            self.x += self.move[0]
            self.y += self.move[1]

        self.rect = pygame.Rect([self.x, self.y, TILESIZE, TILESIZE])
