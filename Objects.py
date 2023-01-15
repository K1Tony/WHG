import pygame as pg
import constants as c
import math


class Player:
    def __init__(self, x: int, y: int, bounds: list[pg.Rect], width: int = c.PLAYER, height: int = c.PLAYER):
        self.width, self.height = width, height
        self.spawn = x, y
        self.x, self.y = x, y
        self.bounds = bounds
        self.speed = 4 * c.SPEED
        self.pad = c.PAD
        self.x_dir = 0
        self.y_dir = 0
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.small_rect = pg.Rect((self.rect.x + self.pad, self.rect.y + self.pad, self.rect.width - 2 * self.pad,
                                   self.rect.height - 2 * self.pad))
        self.color = c.RED

    def __call__(self, window: pg.Surface):
        pg.draw.rect(window, c.BLACK, self.rect)
        pg.draw.rect(window, self.color, self.small_rect)

    def move(self):
        x_cond = False
        for bound in self.bounds:
            if bound.x <= self.rect.x + self.x_dir * self.speed and self.rect.x + self.rect.width + self.x_dir * self.speed <= bound.x + bound.width\
                    and bound.y <= self.rect.y and bound.y + bound.height >= self.rect.y + self.rect.height:
                x_cond = True
                break
            if bound == self.bounds[-1]:
                x_cond = False
        y_cond = False
        for bound in self.bounds:
            if bound.y <= self.rect.y + self.y_dir * self.speed and self.rect.y + self.rect.height + self.y_dir * self.speed <= bound.y + bound.height\
                    and bound.x <= self.rect.x and bound.x + bound.width >= self.rect.x + self.rect.width:
                y_cond = True
                break
            if bound == self.bounds[-1]:
                y_cond = False
        if x_cond:
            self.rect.x += self.x_dir * self.speed
            self.small_rect = self.small_rect = pg.Rect((self.rect.x + self.pad, self.rect.y + self.pad, self.rect.width - 2 * self.pad,
                                                         self.rect.height - 2 * self.pad))
        if y_cond:
            self.rect.y += self.y_dir * self.speed
            self.small_rect = self.small_rect = pg.Rect((self.rect.x + self.pad, self.rect.y + self.pad, self.rect.width - 2 * self.pad,
                                                         self.rect.height - 2 * self.pad))


class Checkpoint:
    def __init__(self, x: int, y: int, width: int = c.CHECKPOINT, height: int = c.CHECKPOINT):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)

    def __call__(self, window: pg.Surface):
        pg.draw.rect(window, c.GREEN, self.rect)

    def save(self, player: Player):
        return 0 <= player.rect.x - self.x <= self.width and 0 <= player.rect.y - self.y <= self.height


class Finish(Checkpoint):
    def __init__(self, x: int, y: int, width: int = c.CHECKPOINT, height: int = c.CHECKPOINT):
        super().__init__(x, y, width, height)

    def save(self, player: Player):
        pass

    def finished(self, player: Player) -> bool:
        return self.rect.colliderect(player.rect)


class Enemy(Player):
    def __init__(self, x: int, y: int, bounds: list[pg.Rect], x_dir: int, y_dir: int, speed: float,
                 checkpoints: list[Checkpoint | Finish],
                 width: int = c.ENEMY, height: int = c.ENEMY):
        super().__init__(x, y, bounds, width, height)
        self.x_dir = x_dir
        self.y_dir = y_dir
        self.color = c.BLUE
        self.speed = speed
        self.checkpoints = checkpoints

    def __call__(self, window: pg.Surface):
        pg.draw.circle(window, c.BLACK, (self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2),
                       self.rect.width // 2)
        pg.draw.circle(window, self.color, (self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2),
                       self.rect.width // 2 - self.pad)

    def move(self):
        if not any(map(lambda x: self.rect.x + self.x_dir * self.speed >= x.x and self.rect.y + self.y_dir * self.speed > x.y\
                       and self.rect.x + self.width + self.x_dir * self.speed <= x.x + x.width and\
                       self.rect.y + self.height + self.y_dir * self.speed <= x.y + x.height, self.bounds)):
            if any(map(lambda x: self.rect.x + self.x_dir * self.speed <= x.x < self.rect.x +
                                    self.width + self.x_dir * self.speed, self.bounds)) and self.x_dir == -1:
                self.x_dir = 1
            elif any(map(lambda x: self.rect.x + self.width + self.x_dir * self.speed > x.x + x.width > self.rect.x +
                                   self.x_dir * self.speed, self.bounds)) and self.x_dir == 1:
                self.x_dir = -1
            if any(map(lambda x: self.rect.y + self.y_dir * self.speed < x.y < self.rect.y + self.height + self.y_dir *
                                 self.speed, self.bounds)) and self.y_dir == -1:
                self.y_dir = 1
            elif any(map(lambda x: self.rect.y + self.height + self.y_dir * self.speed >= x.y + x.height > self.rect.y +
                                   self.y_dir * self.speed, self.bounds)) and self.y_dir == 1:
                self.y_dir = -1
        for checkpoint in self.checkpoints:
            if checkpoint.rect.colliderect(self.rect):
                if self.rect.x < checkpoint.x + checkpoint.width and self.rect.y + self.height > checkpoint.y and\
                 self.rect.y < checkpoint.y + checkpoint.height and self.rect.x + self.width > checkpoint.x +\
                        checkpoint.width and self.x_dir == -1:
                    self.x_dir = 1
                elif self.rect.x + self.width > checkpoint.x and self.rect.y + self.height > checkpoint.y and\
                        self.rect.y <= checkpoint.y + checkpoint.height and self.rect.x < checkpoint.x and\
                        self.x_dir == 1:
                    self.x_dir = -1
                elif self.rect.y < checkpoint.y + checkpoint.height and self.rect.x + self.width > checkpoint.x and\
                        self.rect.x < checkpoint.x + checkpoint.width and self.rect.y + self.height > checkpoint.y + \
                        checkpoint.height and self.y_dir == -1:
                    self.y_dir = 1
                elif self.rect.y + self.height > checkpoint.y and self.rect.x + self.width > checkpoint.x and\
                        self.rect.x < checkpoint.x + checkpoint.width and self.rect.y < checkpoint.y and\
                        self.y_dir == 1:
                    self.y_dir = -1
        self.rect.x += self.x_dir * self.speed
        self.rect.y += self.y_dir * self.speed


class CircularEnemy(Enemy):
    def __init__(self, bounds: list[pg.Rect], speed: float, dst_x: float, dst_y: float, angle: float = 0,
                 omega: float = 0.1, width: int = c.ENEMY, height: int = c.ENEMY, x_dir: int = 0, y_dir: int = 0,
                 x: int = 0, y: int = 0, reverse: bool = False, checkpoints: list[Checkpoint | Finish] = None):
        super(CircularEnemy, self).__init__(x=x, y=y, bounds=bounds, speed=speed, checkpoints=checkpoints,
                                            width=width, height=height, x_dir=x_dir, y_dir=y_dir)
        self.angle = angle
        self.omega = omega
        self.dst_x = dst_x
        self.dst_y = dst_y
        self.reverse = reverse

    def move(self):
        if self.reverse:
            x, y = math.cos(self.angle), math.sin(self.angle)
        else:
            x, y = math.sin(self.angle), math.cos(self.angle)
        self.rect.x = x * self.speed + self.dst_x + self.width // 2
        self.rect.y = y * self.speed + self.dst_y + self.height // 2
        self.angle += self.omega


class Coin(Enemy):
    def __init__(self, x: int, y: int, bounds: list[pg.Rect] = None, checkpoints: list[Checkpoint] = None,
                 width: int = c.ENEMY, height: int = c.ENEMY, x_dir: int = None, y_dir: int = None,
                 speed: float = None):
        super().__init__(x, y, bounds, x_dir, y_dir, speed, checkpoints, width, height)
        self.collected = False
        self.color = c.YELLOW

    def move(self):
        pass
