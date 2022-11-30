import pygame
from tiles import *


class Level:
    def __init__(self, levelData, surface):
        self.levelData = levelData
        self.surface = surface
