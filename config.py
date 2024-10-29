from random import randint


#размер поля
WIDTH = 400
HEIGHT = 400

#параметры игры
SEGMENT_SIZE = 40
DELAY = 300

#словарь для движений
DIRECTIONS = {
    'Up': (0, -1),
    'Down': (0, 1),
    'Left': (-1, 0),
    'Right': (1,0)
}

snake = [(0,0)]
direction = DIRECTIONS['Right']
food = (randint(0,(WIDTH-SEGMENT_SIZE) // SEGMENT_SIZE) * SEGMENT_SIZE,
        randint(0, (HEIGHT-SEGMENT_SIZE) // SEGMENT_SIZE) * SEGMENT_SIZE)
