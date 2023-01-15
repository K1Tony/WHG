from Objects import *
import constants as c

SPEEDS = {1: 7 * c.SPEED,
          2: 6 * c.SPEED,
          3: 6 * c.SPEED,
          5: 7 * c.SPEED,
          }

BOUNDS = {1: [pg.Rect(c.WIDTH // 6, c.HEIGHT // 6, 2 * c.WIDTH // 3, 2 * c.HEIGHT // 3),
              pg.Rect(c.WIDTH // 6 - c.CHECKPOINT, c.HEIGHT // 2 - c.CHECKPOINT // 2, 2 * (c.WIDTH // 3 + c.CHECKPOINT),
                      c.CHECKPOINT)],
          2: [pg.Rect(c.WIDTH // 6, c.HEIGHT // 6, 2 * c.WIDTH // 3, 2 * c.HEIGHT // 3),
              pg.Rect(c.WIDTH // 6 - c.CHECKPOINT, 5 * c.HEIGHT // 6 - c.CHECKPOINT, 2 * c.CHECKPOINT, c.CHECKPOINT),
              pg.Rect(5 * c.WIDTH // 6 - c.CHECKPOINT, c.HEIGHT // 6, 2 * c.CHECKPOINT, c.CHECKPOINT)],
          3: [pg.Rect(c.WIDTH // 6, c.HEIGHT // 6, 2 * c.WIDTH // 3, 2 * c.HEIGHT // 3)],
          4: [pg.Rect(c.WIDTH // 2 - c.CHECKPOINT // 2, c.HEIGHT // 6 - c.CHECKPOINT, c.CHECKPOINT,
                      2 * c.HEIGHT // 3 + 2 * c.CHECKPOINT),
              pg.Rect(c.WIDTH // 2 - 3 * c.CHECKPOINT // 2, c.HEIGHT // 6, 3 * c.CHECKPOINT,
                      2 * c.HEIGHT // 3),
              pg.Rect(c.WIDTH // 2 - 5 * c.CHECKPOINT // 2, c.HEIGHT // 6 + c.CHECKPOINT, 5 * c.CHECKPOINT,
                      2 * c.HEIGHT // 3 - 2 * c.CHECKPOINT),
              pg.Rect(c.WIDTH // 2 - 7 * c.CHECKPOINT // 2, c.HEIGHT // 2 - c.CHECKPOINT // 2, 7 * c.CHECKPOINT,
                      c.CHECKPOINT)],
          5: [pg.Rect(c.WIDTH // 8, c.HEIGHT // 8, 3 * c.WIDTH // 4 + c.CHECKPOINT, c.CHECKPOINT),
              pg.Rect(7 * c.WIDTH // 8 - c.CHECKPOINT, c.HEIGHT // 8, c.CHECKPOINT, 3 * c.HEIGHT // 4),
              pg.Rect(c.WIDTH // 8, 7 * c.HEIGHT // 8 - c.CHECKPOINT, 3 * c.WIDTH // 4 + c.CHECKPOINT, c.CHECKPOINT),
              pg.Rect(c.WIDTH // 8 + c.CHECKPOINT, c.HEIGHT // 8 + 3 * c.CHECKPOINT // 2, c.CHECKPOINT,
                      3 * c.HEIGHT // 4 - 3 * c.CHECKPOINT // 2),
              pg.Rect(c.WIDTH // 8 + c.CHECKPOINT, c.HEIGHT // 8 + 3 * c.CHECKPOINT // 2,
                      3 * c.WIDTH // 4 - 5 * c.CHECKPOINT // 2, c.CHECKPOINT),
              pg.Rect(7 * c.WIDTH // 8 - 5 * c.CHECKPOINT // 2, c.HEIGHT // 8 + 3 * c.CHECKPOINT // 2, c.CHECKPOINT,
                      5 * c.CHECKPOINT // 2),
              pg.Rect(7 * c.WIDTH // 8 - 9 * c.CHECKPOINT // 2, c.HEIGHT // 8 + 3 * c.CHECKPOINT, 3 * c.CHECKPOINT,
                      c.CHECKPOINT)]
          }

FINISHES = {1: Finish(5 * c.WIDTH // 6, c.HEIGHT // 2 - c.CHECKPOINT // 2),
            2: Finish(5 * c.WIDTH // 6, c.HEIGHT // 6),
            3: Finish(5 * c.WIDTH // 6 - c.CHECKPOINT, c.HEIGHT // 6),
            4: Finish(c.WIDTH // 2 - 7 * c.CHECKPOINT // 2, c.HEIGHT // 2 - c.CHECKPOINT // 2),
            5: Finish(7 * c.WIDTH // 8 - 5 * c.CHECKPOINT, c.HEIGHT // 8 + 3 * c.CHECKPOINT)
            }

CHECKPOINTS = {1: [Checkpoint(c.WIDTH // 6 - c.CHECKPOINT, c.HEIGHT // 2 - c.CHECKPOINT // 2), FINISHES[1]],
               2: [Checkpoint(c.WIDTH // 6 - c.CHECKPOINT, 5 * c.HEIGHT // 6 - c.CHECKPOINT), FINISHES[2]],
               3: [Checkpoint(c.WIDTH // 6, 5 * c.HEIGHT // 6 - c.CHECKPOINT, c.CHECKPOINT, c.CHECKPOINT), FINISHES[3]],
               4: [Checkpoint(c.WIDTH // 2 - c.CHECKPOINT // 2, c.HEIGHT // 6 - c.CHECKPOINT),
                   Checkpoint(c.WIDTH // 2 + 5 * c.CHECKPOINT // 2, c.HEIGHT // 2 - c.CHECKPOINT // 2),
                   Checkpoint(c.WIDTH // 2 - c.CHECKPOINT // 2, 5 * c.HEIGHT // 6),
                   FINISHES[4]],
               5: [Checkpoint(c.WIDTH // 8, c.HEIGHT // 8), Checkpoint(7 * c.WIDTH // 8, c.HEIGHT // 8),
                   Checkpoint(c.WIDTH // 8, 7 * c.HEIGHT // 8 - c.CHECKPOINT),
                   Checkpoint(7 * c.WIDTH // 8, 7 * c.HEIGHT // 8 - c.CHECKPOINT),
                   Checkpoint(7 * c.WIDTH // 8 - 5 * c.CHECKPOINT // 2, c.HEIGHT // 8 + 5 * c.CHECKPOINT // 2,
                              height=c.CHECKPOINT // 2)]
               }

ENEMIES = {1: [Enemy(c.WIDTH // 6, c.HEIGHT // 6, BOUNDS[1], -1, 1, SPEEDS[1], CHECKPOINTS[1]),
               Enemy(5 * c.WIDTH // 6 - c.ENEMY, c.HEIGHT // 6, BOUNDS[1], -1, 1, SPEEDS[1], CHECKPOINTS[1]),
               Enemy(c.WIDTH // 6, 5 * c.HEIGHT // 6 - c.ENEMY, BOUNDS[1], 1, -1, SPEEDS[1], CHECKPOINTS[1]),
               Enemy(5 * c.WIDTH // 6 - c.ENEMY, 5 * c.HEIGHT // 6 - c.ENEMY, BOUNDS[1], -1, -1, SPEEDS[1], CHECKPOINTS[1])],
           2: [Enemy(c.WIDTH // 18 * (i + 3) + c.PAD, [c.HEIGHT // 6, 5 * c.HEIGHT // 6 - c.ENEMY][i % 2],
                     BOUNDS[2], 0, [1, -1][i % 2], SPEEDS[2], CHECKPOINTS[2]) for i in range(12)],
           3: [Enemy(c.WIDTH // 6 + c.PAD, c.HEIGHT // 6, BOUNDS[3], 0, 1, SPEEDS[3], CHECKPOINTS[3]),
               Enemy(c.WIDTH // 6 + c.ENEMY + c.PAD, c.HEIGHT // 6, BOUNDS[3], 0, 1, SPEEDS[3], CHECKPOINTS[3]),
               Enemy(5 * c.WIDTH // 6 - 2 * c.ENEMY, 5 * c.HEIGHT // 6 - c.ENEMY, BOUNDS[3], 0, -1, SPEEDS[3], CHECKPOINTS[3]),
               Enemy(5 * c.WIDTH // 6 - c.ENEMY, 5 * c.HEIGHT // 6 - c.ENEMY, BOUNDS[3], 0, -1, SPEEDS[3], CHECKPOINTS[3])] +
              [CircularEnemy(BOUNDS[3], 200 * c.SPEED, c.WIDTH // 2 - c.ENEMY, c.HEIGHT // 2 - c.ENEMY,
                             angle=i * math.pi / 5, omega=0.02) for i in range(10)],
           4: [Enemy(c.WIDTH // 2 - c.ENEMY // 2, c.HEIGHT // 2 - c.ENEMY // 2, BOUNDS[4], 0, 0, 0,
                     CHECKPOINTS[4])] + [CircularEnemy(BOUNDS[4], (i - i % 4) * c.SPEED * 10, c.WIDTH // 2 -
                                                       c.ENEMY, c.HEIGHT // 2 - c.ENEMY,
                                                       angle=[3 * math.pi / 4, -math.pi / 4, math.pi / 4, 5 * math.pi / 4]
                                                       [i % 4], omega=0.04, reverse=True) for i in range(1, 24)],
           5: [Enemy(c.WIDTH // 8 + c.CHECKPOINT + c.PAD, c.HEIGHT // 8 + c.PAD, BOUNDS[5], 1, 0, SPEEDS[5],
                     CHECKPOINTS[5]),
               Enemy(7 * c.WIDTH // 8 - c.ENEMY - c.PAD, c.HEIGHT // 8 + c.CHECKPOINT - c.ENEMY - c.PAD,
                     BOUNDS[5], -1, 0, SPEEDS[5], CHECKPOINTS[5]),
               Enemy(7 * c.WIDTH // 8 - c.CHECKPOINT + c.PAD, c.HEIGHT // 8 + c.PAD, BOUNDS[5], 0, 1, SPEEDS[5],
                     CHECKPOINTS[5]),
               Enemy(7 * c.WIDTH // 8 - c.ENEMY - c.PAD, 7 * c.HEIGHT // 8 - c.ENEMY - c.PAD, BOUNDS[5],
                     0, -1, SPEEDS[5], CHECKPOINTS[5]),
               Enemy(c.WIDTH // 8 + c.CHECKPOINT + c.PAD, 7 * c.HEIGHT // 8 - c.ENEMY - c.PAD, BOUNDS[5],
                     1, 0, SPEEDS[5], CHECKPOINTS[5]),
               Enemy(7 * c.WIDTH // 8 - c.PAD - c.ENEMY, 7 * c.HEIGHT // 8 + c.PAD - c.CHECKPOINT, BOUNDS[5],
                     -1, 0, SPEEDS[5], CHECKPOINTS[5]),
               Enemy(c.WIDTH // 8 + c.CHECKPOINT + c.PAD, 7 * c.HEIGHT // 8 - c.ENEMY - c.PAD, BOUNDS[5],
                     0, -1, SPEEDS[5] // 1.5, CHECKPOINTS[5]),
               Enemy(c.WIDTH // 8 + 2 * c.CHECKPOINT - c.ENEMY - c.PAD, c.HEIGHT // 8 + 3 * c.CHECKPOINT // 2 + c.PAD,
                     BOUNDS[5], 0, 1, SPEEDS[5] // 1.5, CHECKPOINTS[5]),
               Enemy(c.WIDTH // 8 + c.CHECKPOINT + c.PAD, c.HEIGHT // 8 + 3 * c.CHECKPOINT // 2 + c.PAD, BOUNDS[5],
                     1, 0, SPEEDS[5] // 1.2, CHECKPOINTS[5]),
               Enemy(7 * c.WIDTH // 8 - 3 * c.CHECKPOINT // 2 - c.PAD - c.ENEMY, c.HEIGHT // 8 + 5 * c.CHECKPOINT // 2
                     - c.ENEMY - c.PAD, BOUNDS[5], -1, 0, SPEEDS[5] // 1.2, CHECKPOINTS[5])] +
           [CircularEnemy(BOUNDS[5], 50 * c.SPEED, 7 * c.WIDTH // 8 - 7 * c.CHECKPOINT // 2,
                          c.HEIGHT // 8 + 3 * c.CHECKPOINT + c.PAD * 3, angle=i * math.pi,
                          omega=0.04) for i in range(2)]
           }

COINS = {1: [],
         2: [],
         3: [Coin(c.WIDTH // 2 - c.ENEMY // 2, c.HEIGHT // 2 - c.ENEMY // 2)],
         4: [Coin(c.WIDTH // 2 - c.ENEMY // 2, c.HEIGHT // 2 - 6 * c.ENEMY), Coin(c.WIDTH // 2 + 5 * c.ENEMY,
                                                                                  c.HEIGHT // 2 - c.ENEMY // 2),
             Coin(c.WIDTH // 2 - c.ENEMY // 2, c.HEIGHT // 2 + 5 * c.ENEMY)],
         5: []
         }
