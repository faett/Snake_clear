from tkinter import *
from config import *
from random import randint

root = Tk()
root.title('Clear Snake Udsu')
root.geometry('400x400')

canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg='green')
canvas.pack()
score_label = Label(root, text="Score: 0", font=("Arial", 14))
score_label.pack()
score = 0

snake = [(WIDTH // 2, HEIGHT // 2)]
direction = DIRECTIONS['Right']
food = (randint(0, (WIDTH - SEGMENT_SIZE) // SEGMENT_SIZE) * SEGMENT_SIZE,
        randint(0, (HEIGHT - SEGMENT_SIZE) // SEGMENT_SIZE) * SEGMENT_SIZE)
game_over_flag = False
restart_button = None

def update_snake():
    global snake, food, score, game_over_flag
    if game_over_flag:
        return

    new_head = (snake[0][0] + direction[0] * SEGMENT_SIZE,
                snake[0][1] + direction[1] * SEGMENT_SIZE)

    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
        new_head in snake):
        show_game_over()
        return

    snake = [new_head] + snake

    if new_head == food:
        score += 1
        score_label.config(text=f"Score: {score}")
        create_food()
    else:
        snake.pop()

    draw_game()
    root.after(DELAY, update_snake)

def change_directions(new_direction):
    global direction
    if (direction[0] * -1, direction[1] * -1) != new_direction:
        direction = new_direction

def draw_game():
    canvas.delete('all')
    canvas.create_oval(food[0], food[1], food[0] + SEGMENT_SIZE, food[1] + SEGMENT_SIZE, fill='red')
    for x, y in snake:
        canvas.create_oval(x, y, x + SEGMENT_SIZE, y + SEGMENT_SIZE, fill='yellow')

def show_game_over():
    global game_over_flag, restart_button
    game_over_flag = True
    canvas.delete('all')
    canvas.create_text(WIDTH // 2, HEIGHT // 2 - 20, text="Game Over", fill="white", font=("Arial", 24))
    canvas.create_text(WIDTH // 2, HEIGHT // 2 + 20, text=f"Final Score: {score}", fill="white", font=("Arial", 14))

    restart_button = Button(root, text="Restart", command=restart_game)
    restart_button.place(x=WIDTH // 2 - 30, y=HEIGHT // 2 + 50)  # Adjust button position as needed

def create_food():
    global food
    food = (randint(0, (WIDTH - SEGMENT_SIZE) // SEGMENT_SIZE) * SEGMENT_SIZE,
            randint(0, (HEIGHT - SEGMENT_SIZE) // SEGMENT_SIZE) * SEGMENT_SIZE)

def restart_game():
    global snake, direction, score, game_over_flag, restart_button
    snake = [(WIDTH // 2, HEIGHT // 2)]
    direction = DIRECTIONS['Right']
    score = 0
    game_over_flag = False
    score_label.config(text="Score: 0")
    create_food()
    draw_game()
    update_snake()
    if restart_button:
        restart_button.destroy()
        restart_button = None

root.bind('<Up>', lambda event: change_directions(DIRECTIONS['Up']))
root.bind('<Down>', lambda event: change_directions(DIRECTIONS['Down']))
root.bind('<Left>', lambda event: change_directions(DIRECTIONS['Left']))
root.bind('<Right>', lambda event: change_directions(DIRECTIONS['Right']))

create_food()
draw_game()
update_snake()
root.mainloop()
