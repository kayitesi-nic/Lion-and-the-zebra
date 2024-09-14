import pgzrun
from random import randint

WIDTH= 600
HEIGHT= 600
TITLE= "lion and the zebra"

lion= Actor("lion")
lion.pos= 100,100

zebra= Actor("zebra")
zebra.pos= 50,50

score= 0
game_over= False

def draw():
    screen.blit("background image",(0,0))
    lion.draw()
    zebra.draw()

    screen.draw.text("Score:" +str(score), topleft= (30,30), color=("black"), fontsize=40)

    if game_over:
        screen.fill("pink")
        screen.draw.text("Time's up! Your Score is:" +str(score), color=("red"), topleft= (200,200))

def place_zebra():
    zebra.x= randint(50,WIDTH-50)
    zebra.y= randint(50,HEIGHT-50)

def time_up():
    global game_over
    game_over= True 

def update():
    global score
    
    if keyboard.left:
        lion.x= lion.x-2
    if keyboard.right:
        lion.x= lion.x+2
    if keyboard.up:
        lion.y= lion.y-2
    if keyboard.down:
        lion.y= lion.y+2

    zebra_touched= lion.colliderect(zebra)
    if zebra_touched:
        score= score+10
        place_zebra()

clock.schedule(time_up, 15)


pgzrun.go()