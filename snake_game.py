import random
from tkinter import *


SPACE_SIZE = 50
GAME_WIDTH = 800
GAME_HEIGHT = 800
SNAKE_BODY = 4
GAME_SPEED = 60


class Snake():
    
    def __init__ (self):
        self.body_size = SNAKE_BODY
        self.coordinates = []
        self.squares = []

        for i in range(0, SNAKE_BODY):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            square =  canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE, fill = 'green', tag= 'snake')
            self.squares.append(square)


class Food():
    
    def __init__(self):
         x = random.randint(0, (GAME_WIDTH/SPACE_SIZE-1)) * SPACE_SIZE
         y= random.randint(0, (GAME_HEIGHT/SPACE_SIZE-1)) * SPACE_SIZE

         self.coordinates = [x,y]

         canvas.create_oval(x,y, x+SPACE_SIZE, y+SPACE_SIZE, fill = 'red', tag = 'food')

def turns(snake, food):
    x,y = snake.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0,(x,y))
    square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill = 'green')
    snake.squares.insert(0,square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score +=1

        label.config(text = "score:{}".format(score))

        canvas.delete("food")
        food = Food()    
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        pass


    root.after(GAME_SPEED, turns, snake, food )

def change_direction(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_collisions(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font = ('consolas',70), text ='GAME OVER', fill = 'red', tag = 'gameover')

    # label = Label(canvas, text = 'Restart? type \'y\' or \'n\'', font=('consolas',40))
    # label.pack(side='bottom')

root = Tk(className='Snake on Python :^)')
root.resizable(False, False)

score = 0
direction = 'down'

frame = Frame(root, relief = 'sunken',
              bd = 2, bg='white')
frame.pack(fill = 'both', expand = True,
           padx = 10, pady = 10)

label = Label(root, text = 'Scoreboard ~~ {}'.format(score),
              font = ('consolas', 32))
label.pack()

canvas = Canvas(root, bg = 'black', height=800,width=800)
canvas.pack()

root.bind('<Left>', lambda event: change_direction('left'))
root.bind('<Right>', lambda event: change_direction('right'))
root.bind('<Up>', lambda event: change_direction('up'))
root.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

turns(snake,food)

root.mainloop()
