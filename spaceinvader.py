import math
import random
import pygame

screenwidth = 800
screenheight = 500
playerstart_x = 370
playerstart_y = 380
enemystart_ymin = 50
enemystart_ymax = 150
enemyspeed_x =4
enemyspeed_y= 40
bulletspeed_y = 40
collision_distance = 27

pygame.init()

screen = pygame.display.set_mode((screenwidth, screenheight))

background = pygame.image.load('backgroujd.png')

pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerimg = pygame.image.load('player.png')
playerx = playerstart_x
playery = playerstart_y
playerx_change = 0

enemyimg = []
enemyx = []
enemyy = []
enemyxchange = []
enemyychange = []
numofenemies = 6

for _i in range(numofenemies):
    enemyimg.append(pygame.image.load("enemy.png"))
    enemyx.append(random.randint(0, screenwidth - 64 ))

    enemyy.append(random.randint(enemystart_ymin,enemystart_ymax))
    