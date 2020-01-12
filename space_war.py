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
        if self.speed > 0:
            self.speed -= 1


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