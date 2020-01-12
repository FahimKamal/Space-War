"""
SpaceWar Game
Created by: Fahim kamal
Date: 12.01.2020
"""
import turtle
import time
import os
import random

# Setup the Screen
window = turtle.Screen()
window.title('SpaceWar by Fahim Kamal')
window.bgcolor('black')
window.setup(width=600, height=600)
window.tracer()

class Sprite(turtle.Turtle):
    def __init__(self, sprite_shape, color, startx, starty):
        turtle.Turtle.__init__(self, shape=sprite_shape)
        # self.shape(sprite_shape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.goto(startx, starty)
        self.speed = 1

    def move(self):
        # forward() function moves the turtle forward
        self.forward(self.speed)
        # Border detection
        if self.xcor() > 240:
            # Turn around when hit right border
            self.right(60)
        if self.xcor() < -240:
            # Turn around when hit left border
            self.right(60)
        if self.ycor() > 240:
            # Turn around when hit top border
            self.left(60)
        if self.ycor() < -240:
            # Turn around when hit bottom border
            self.left(60)

class Player(Sprite):
    def __init__(self, sprite_shape, color, startx, starty):
        Sprite.__init__(self,sprite_shape,color, startx, starty)
        self.speed = 1
        self.lives = 3

    def turn_left(self):
        """Turns the turtle by 45 degree to the left"""
        self.left(45)

    def turn_right(self):
        """Turns the turtle by 45 degree to the right"""
        self.right(45)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        # if self.speed > 0:
        self.speed -= 1


class Game:
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = 'playing'
        self.pen = turtle.Turtle()
        self.lives = 3

    def draw_border(self):
        """Draw border"""
        self.pen.speed(0)
        self.pen.color('white')
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-250, 250)
        self.pen.pendown()
        for _ in range(4):
            self.pen.forward(500)
            self.pen.right(90)
        self.pen.penup()
        self.pen.hideturtle()


# Create the Game object
game = Game()
# Draw the border
game.draw_border()

# Create my player
player = Player('triangle', 'white', 0, 0)

# Keyboard binding
window.listen()
window.onkeypress(player.turn_left, 'Left')
window.onkeypress(player.turn_right, 'Right')
window.onkeypress(player.accelerate, 'Up')
window.onkeypress(player.decelerate, 'Down')

# Main game loop
while True:
    player.move()