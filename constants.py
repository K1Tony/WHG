import pygame as pg
from pyautogui import size

pg.font.init()

"""
GAME PARAMETERS
"""
FPS = 60

"""
DIMENSIONS
"""
ABS_W, ABS_H = size()
CLASSIC = ABS_W // 2, 2 * ABS_H // 3
WIDTH, HEIGHT = CLASSIC
PLAYER = WIDTH // 27
ENEMY = WIDTH // 30
CHECKPOINT = WIDTH // 10
PAD = PLAYER // 8

"""
COLORS
"""
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (50, 255, 160)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

GREY = (128, 128, 128)
DARK_GREY = (80, 80, 80)
LIGHT_GREY = (170, 170, 170)

VIOLET = (128, 0, 255)

LIGHT_VIOLET = (190, 190, 255)

"""
EVENTS
"""
NEXT = pg.USEREVENT + 1

"""
FONTS
"""
LEVEL_NUM = pg.font.SysFont('Arial', 50)
DEATH_COUNT = pg.font.SysFont('Arial', 40, bold=True)
CHEAT = pg.font.SysFont('Arial', 20)

"""
OTHER
"""
SPEED = WIDTH // (10 * FPS)
