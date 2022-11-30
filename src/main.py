# https://www.youtube.com/watch?v=YWN8GcmJ-jA&t=1384s

import pygame
from typing import List

from map import *
from tiles import *


pygame.init()

FPS = 30  # frames per second setting
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Space Invaders")

# Tile map
testTileGroup = pygame.sprite.Group(Tile(0, 0, 32, 32, "red"))


playerImg = pygame.image.load("src/img/mario.png")
playerX = 370
playerY = 480
playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    player(playerX, playerY)

    testTileGroup.draw(screen)

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()
