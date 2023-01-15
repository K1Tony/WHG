from Objects import *

pg.init()


def set_background(window: pg.Surface, bounds: list[pg.Rect], player: Player, enemies: list[Enemy], coins: list[Coin],
                   checkpoints: list[Checkpoint], finish: Finish, level: pg.Surface, deaths: pg.Surface, cheat: bool,
                   text_box: pg.Surface, cheat_area: pg.Rect)\
        -> None:
    window.fill(c.LIGHT_VIOLET)

    window.blit(level, (c.WIDTH - level.get_width(), 0))
    window.blit(deaths, (0, 0))

    for bound in bounds:
        pg.draw.rect(window, c.WHITE, bound)

    for checkpoint in checkpoints:
        checkpoint(window)

    finish(window)

    player(window)
    if not cheat:
        player.move()

    for coin in coins:
        if not coin.collected:
            coin(window)
        if player.rect.colliderect(coin.rect):
            coin.collected = True

    for enemy in enemies:
        enemy(window)
        if not cheat:
            enemy.move()

    if player.rect.colliderect(finish.rect) and all(map(lambda x: x.collected, coins)):
        pg.event.post(pg.event.Event(c.NEXT))

    pg.draw.rect(window, c.BLACK, cheat_area)
    window.blit(text_box, (0, 0))
    pg.display.update()
