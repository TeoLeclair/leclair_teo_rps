# this file was created by: Teo Leclair

'''
Goals - create images for paper and scissors
Write program so that user selects rock or paper or scissors when cliking on image...
'''

# import package
import turtle
from turtle import *
# The os module allows us to access the current directory in order to access assets
import os
import winsound
print("The current working directory is (getcwd): " + os.getcwd())
print("The current working directory is (path.dirname): " + os.path.dirname(__file__))

from random import randint
from time import sleep
# setup the game folders using the os module
game_folder = os.path.dirname(__file__)
images_folder = os.path.join(game_folder, 'images')
sounds_folder = os.path.join(game_folder, 'sounds')

# setup the width and height for the window
WIDTH, HEIGHT = 1000, 400

rock_w, rock_h = 256, 280

paper_w, paper_h = 256, 204

scissors_w, scissors_h = 256, 170

player_choice = ""

cpu_choice = ""

# setup the Screen class using the turtle module
screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)  # fudge factors due to window borders & title bar
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth=WIDTH, canvheight=HEIGHT, bg="lightblue")


# canvas object
cv = screen.getcanvas()
# hack to make window not resizable for more reliable coordinates
cv._rootwindow.resizable(False, False)

# setup the rock image using the os module as rock_image
rock_image = os.path.join(images_folder, 'rock.gif')
rock_instance = turtle.Turtle()
# rock_instance.hideturtle()

cpu_rock_image = os.path.join(images_folder, 'cpu_rock.gif')
cpu_rock_instance = turtle.Turtle()
# cpu_rock_instance.hideturtle()

paper_image = os.path.join(images_folder, 'paper.gif')
paper_instance = turtle.Turtle()
# paper_instance.hideturtle()

cpu_paper_image = os.path.join(images_folder, 'cpu_paper.gif')
cpu_paper_instance = turtle.Turtle()
# cpu_paper_instance.hideturtle()

scissors_image = os.path.join(images_folder, 'scissors.gif')
scissors_instance = turtle.Turtle()
# scissors_instance.hideturtle()

cpu_scissors_image = os.path.join(images_folder, 'cpu_scissors.gif')
cpu_scissors_instance = turtle.Turtle()
# cpu_scissors_instance.hideturtle()

def show_rock(x,y):
    # add the rock image as a shape
    screen.addshape(rock_image)
    # attach the rock_image to the rock_instance
    rock_instance.shape(rock_image)
    # remove the pen option from the rock_instance so it doesn't draw lines when moved
    rock_instance.penup()
    # set the position of the rock_instance
    rock_instance.setpos(x,y)

def cpu_show_rock(x,y):
    screen.addshape(cpu_rock_image)
    cpu_rock_instance.shape(cpu_rock_image)
    cpu_rock_instance.penup()
    cpu_rock_instance.setpos(x,y)

def show_paper(x,y):
    screen.addshape(paper_image)
    paper_instance.shape(paper_image)
    paper_instance.penup()
    paper_instance.setpos(x,y)

def cpu_show_paper(x,y):
    screen.addshape(cpu_paper_image)
    cpu_paper_instance.shape(cpu_paper_image)
    cpu_paper_instance.penup()
    cpu_paper_instance.setpos(x,y)

def show_scissors(x,y):
    screen.addshape(scissors_image)
    scissors_instance.shape(scissors_image)
    scissors_instance.penup()
    scissors_instance.setpos(x,y)

def cpu_show_scissors(x,y):
    screen.addshape(cpu_scissors_image)
    cpu_scissors_instance.shape(cpu_scissors_image)
    cpu_scissors_instance.penup() #penup allows to have the words show up on turtle
    cpu_scissors_instance.setpos(x,y)
# defining both cpu and player options
text = turtle.Turtle()
# defining type and what its specifics will be when dispalyed
def write_text(message, x, y):
    text.hideturtle()
    text.color('red')
    text.penup()
    text.clear()
    text.setpos(x,y)
    text.write(message, False, "center", ("Arial", 24, "normal"))
    # for i in message:
    #     text.setpos(x,y)
    #     text.write(i, False, "center", ("Arial", 24, "normal"))    
    #     x += 17
    #     sleep(.01)
        

def cpu_select():
    choices = ["rock", "paper", "scissors"]
    return choices[randint(0,2)]
# this funcion allows for the cpu to make random choices
# this function uses and x y value, an obj
def collide(x,y,obj,w,h):
    if x < obj.pos()[0] + w/2 and x > obj.pos()[0] -  w/2 and y < obj.pos()[1] + h/2 and y > obj.pos()[1] - h/2:
        return True
    else:
        return False

show_rock(-300,0)
show_paper(0,0)
show_scissors(300,0)
# coordinates where to have images start
# logic below explaining what happens with each decision and the result of cpu and player and where to move image

import time
time.sleep(1)
# one second pause time for words to show neatly and not overlap
def mouse_pos(x, y):
    # prints whatever the cpu chooses
    print(cpu_select())
    # this is grabbing the cpu choice
    cpu_picked = cpu_select()
    # explains what to do when the player chooses rock
    if collide(x,y,rock_instance,rock_w,rock_h):
        # what to say and where to say the message
        write_text("You picked ROCK!", 0, 150 )
        # this is checking what the cpu chose
        if cpu_picked == "rock":
            # handles rock vs. rock
            time.sleep(1)
            write_text("The computer chose rock too...", 0, 150)
            show_scissors(2000,0)
            show_paper(2000,0)
            cpu_show_rock(300,0)
            show_rock(-300,0)
            time.sleep(1)
            write_text("It is a tie...", 0, 150 )
        if cpu_picked == "paper":
            # handle paper vs. rock case
            time.sleep(1)
            write_text("The computer chose paper!", 0, 150)
            show_scissors(2000,0)
            show_paper(2000,0)
            cpu_show_paper(300,0)
            show_rock(-300,0)
            time.sleep(1)
            write_text("You lost!", 0, 150)
        if cpu_picked == "scissors":
            # handle scissors vs. rock
            time.sleep(1)
            write_text("The computer chose scissors!", 0, 150)
            show_paper(2000,0)
            show_scissors(2000,0)
            cpu_show_scissors(300,0)
            show_rock(-300,0)
            time.sleep(1)
            write_text("You won!", 0, 150)
    else:
            (x,y,rock_instance,rock_w,rock_h,x,y,paper_instance,paper_w,paper_h,x,y,scissors_instance,scissors_w,scissors_h)
            write_text("choose something you fool!", 0, 150)
# only need for first instance 
# this takes care of the chance that none of the above conditions are met
    if collide(x,y,paper_instance,paper_w,paper_h):
        write_text("You picked the PAPER!", 0, 150 )
        if cpu_picked == "paper":
            time.sleep(1)
            write_text("The computer chose paper too...", 0, 150)
            show_scissors(2000,0)
            show_rock(2000,0)
            show_paper(-300,0)
            cpu_show_paper(300,0)
            time.sleep(1)
            write_text("It is a tie...", 0, 150 )
        if cpu_picked == "scissors":
            time.sleep(1)
            write_text("The computer chose scissors!", 0, 150)
            show_scissors(2000,0)
            show_rock(2000,0)
            cpu_show_scissors(300,0)
            show_paper(-300,0)
            time.sleep(1)
            write_text("You lost!", 0, 150)
        if cpu_picked == "rock":
            time.sleep(1)
            write_text("The computer chose rock!", 0, 150)
            show_rock(2000,0)
            show_scissors(2000,0)
            cpu_show_rock(300,0)
            show_paper(-300,0)
            time.sleep(1)
            write_text("You won!", 0, 150)
    if collide(x,y,scissors_instance,scissors_w,scissors_h):
        write_text("You picked the scissors!", 0, 150 )
        if cpu_picked == "scissors":
            time.sleep(1)
            write_text("The computer chose scissors too...", 0, 150)
            show_paper(2000,0)
            show_rock(2000,0)
            show_scissors(-300,0)
            cpu_show_scissors(300,0)
            time.sleep(1)
            write_text("It is a tie...", 0, 150 )
        if cpu_picked == "rock":
            time.sleep(1)
            write_text("The computer chose rock!", 0, 150)
            show_paper(2000,0)
            show_rock(2000,0)
            show_scissors(-300,0)
            cpu_show_rock(300,0)
            time.sleep(1)
            write_text("You lost!", 0, 150)
        if cpu_picked == "paper":
            time.sleep(1)
            write_text("The computer chose paper!", 0, 150)
            show_rock(2000,0)
            show_paper(2000,0)
            show_scissors(-300,0)
            cpu_show_paper(300,0)
            time.sleep(1)
            write_text("You won!", 0, 150)
    
    
    
    
    
    
    # if collide:
    #     (x,y,rock_instance,rock_w,rock_h,x,y,paper_instance,paper_w,paper_h,x,y,scissors_instance,scissors_w,scissors_h)
    #     write_text("You chose NOTHING!", 0, 150)
       
    


screen.onclick(mouse_pos)
# runs mainloop for Turtle - required to be last  
write_text("Let's play rock paper scissors...", 0, 150 )


screen.mainloop()


