from tkinter import *

from config import *

from random import randint

root = Tk()
root.title('Clear Snake Udsu')
root.geometry('400x400')
canvas = Canvas(root, width = WIDTH, height = HEIGHT, bg = 'green')
canvas.pack()


def update_snake():
    global snake, food
    new_head = (snake[0][0] + direction[0] * SEGMENT_SIZE,
                snake[0][1] + direction[1] * SEGMENT_SIZE)
    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
        new_head in snake):
        game_over()
        return
    snake = [new_head] + snake

    if new_head == food:
        create_food()
    else:
        snake.pop()
    draw_game()
    root.after(DELAY, update_snake)

def chenge_directions(new_direction):
    global direction
    if (direction[0] * -1, direction[1] * -1) != new_direction:
        direction = new_direction



def draw_game():
    canvas.delete('all')
    canvas.create_oval(food[0], food[1],
                       food[0] + SEGMENT_SIZE, food[1] + SEGMENT_SIZE,
                       fill = 'red')
    for x, y in snake:
        canvas.create_oval(x, y, x + SEGMENT_SIZE, y + SEGMENT_SIZE, fill = 'yellow')


def game_over():
    canvas.delete('all')

def create_food():
    global food
    food = (randint(0, (WIDTH - SEGMENT_SIZE) // SEGMENT_SIZE) * SEGMENT_SIZE,
            randint(0, (HEIGHT - SEGMENT_SIZE) // SEGMENT_SIZE) * SEGMENT_SIZE)


root.bind('<Up>', lambda event: chenge_directions(DIRECTIONS['Up']))
root.bind('<Down>', lambda event: chenge_directions(DIRECTIONS['Down']))
root.bind('<Left>', lambda event: chenge_directions(DIRECTIONS['Left']))
root.bind('<Right>', lambda event: chenge_directions(DIRECTIONS['Right']))


draw_game()
update_snake()
root.mainloop()