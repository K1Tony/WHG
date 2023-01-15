import background as bg
from levels import *
pg.init()


def main() -> None:
    # Game essentials
    run = True
    level = 1
    deaths = 0
    clock = pg.time.Clock()
    spawn = CHECKPOINTS[level][0]
    spawn_point = (spawn.x + spawn.width // 2 - c.PLAYER // 2, spawn.y + spawn.height // 2 - c.PLAYER // 2)
    cheat = False
    text = ''
    info_text = 'Enter cheat code'

    # Cheats
    god = False
    text_box = pg.Surface((0, 0))
    cheat_area = pg.Rect(0, 0, c.WIDTH, c.HEIGHT // 30)

    # Game window
    window = pg.display.set_mode(c.CLASSIC)

    # Player
    player = Player(*spawn_point, BOUNDS[level])

    # Enemies
    enemies = ENEMIES[level]

    # Coins
    coins = COINS[level]

    # Checkpoints
    checkpoints = CHECKPOINTS[level]
    finish = FINISHES[level]

    # Other parameters
    level_num = c.LEVEL_NUM.render(f'Level {level}', True, c.BLACK)
    death_count = c.DEATH_COUNT.render(f'Deaths: {deaths}', True, c.BLACK)

    while run:
        clock.tick(c.FPS)

        # Event loop
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    run = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    for enemy in enemies:
                        if isinstance(enemy, CircularEnemy):
                            enemy.omega += 0.1
                        else:
                            enemy.speed += 0.5
                if event.key == pg.K_LCTRL:
                    cheat = not cheat
                if cheat:
                    cheat_area = pg.Rect(0, 0, c.WIDTH, c.HEIGHT // 15)
                    if event.key == pg.K_BACKSPACE:
                        info_text = ''
                        text = text[:-1]
                    elif event.key == pg.K_RETURN:
                        print(text)
                        if text == 'gamerule.god=True':
                            god = True
                        elif text == 'gamerule.god=False':
                            god = False
                        elif text == 'cheats.disable':
                            god = False
                        elif text == 'gameplay.coins.collect=all':
                            coins.clear()
                        elif text == 'gameplay.enemies.neutralise=all':
                            enemies.clear()
                        elif text[:22] == 'gameplay.level.switch=':
                            if text[22:].isdigit() and int(text[22:]) < 6:
                                level = int(text[22:])
                                level_num = c.LEVEL_NUM.render(f'Level {level}', True, c.BLACK)
                                spawn = CHECKPOINTS[level][0]
                                spawn_point = (
                                    spawn.x + spawn.width // 2 - c.PLAYER // 2,
                                    spawn.y + spawn.height // 2 - c.PLAYER // 2)

                                # Player
                                player.rect.x, player.rect.y = spawn_point
                                player.bounds = BOUNDS[level]

                                # Enemies
                                enemies = ENEMIES[level]

                                # Coins
                                coins = COINS[level]

                                # Checkpoints
                                checkpoints = CHECKPOINTS[level]
                                finish = FINISHES[level]
                                cheat = False
                        elif text == 'gameplay.progress.deaths.remove=all':
                            deaths = 0
                            death_count = c.DEATH_COUNT.render(f'Deaths: {deaths}', True, c.BLACK)
                        text = ''
                    else:
                        info_text = ''
                        text += event.unicode

            if event.type == c.NEXT:
                level += 1
                level_num = c.LEVEL_NUM.render(f'Level {level}', True, c.BLACK)
                if level < 6:
                    spawn = CHECKPOINTS[level][0]
                    spawn_point = (
                        spawn.x + spawn.width // 2 - c.PLAYER // 2, spawn.y + spawn.height // 2 - c.PLAYER // 2)

                    # Player
                    player.rect.x, player.rect.y = spawn_point
                    player.bounds = BOUNDS[level]

                    # Enemies
                    enemies = ENEMIES[level]

                    # Coins
                    coins = COINS[level]

                    # Checkpoints
                    checkpoints = CHECKPOINTS[level]
                    finish = FINISHES[level]
                else:
                    run = False
        if len(info_text) > 0:
            text_box = c.CHEAT.render(info_text, True, c.WHITE)
        else:
            text_box = c.CHEAT.render(text, True, c.WHITE)
        if not cheat:
            cheat_area = pg.Rect(0, 0, 0, 0)
        if not run:
            break

        pressed = pg.key.get_pressed()
        left, up, right_, down_ = pressed[pg.K_a] or pressed[pg.K_LEFT], pressed[pg.K_w] or pressed[pg.K_UP],\
            pressed[pg.K_d] or pressed[pg.K_RIGHT], pressed[pg.K_s] or pressed[pg.K_DOWN]
        if left:
            player.x_dir = -1
        if up:
            player.y_dir = -1
        if right_:
            player.x_dir = 1
        if down_:
            player.y_dir = 1
        if not left and not right_:
            player.x_dir = 0
        if not up and not down_:
            player.y_dir = 0

        for checkpoint in checkpoints:
            if checkpoint.save(player):
                spawn_point = (checkpoint.x + checkpoint.width // 2 - player.width // 2,
                               checkpoint.y + checkpoint.height // 2 - player.height // 2)

        if all(map(lambda x: not player.small_rect.colliderect(x.rect), enemies)) or god:
            bg.set_background(window, BOUNDS[level], player, enemies, coins, checkpoints, finish, level_num,
                              death_count, cheat, text_box, cheat_area)
        else:
            player.rect.x, player.rect.y = spawn_point
            deaths += 1
            death_count = c.DEATH_COUNT.render(f'Deaths: {deaths}', True, c.BLACK)
            for coin in coins:
                coin.collected = False
            bg.set_background(window, BOUNDS[level], player, enemies, coins, checkpoints, finish, level_num,
                              death_count, cheat, text_box, cheat_area)


if __name__ == '__main__':
    main()
