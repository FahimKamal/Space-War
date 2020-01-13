"""
SpaceWar Game
Created by: Fahim kamal
Date: 12.01.2020
"""
import turtle
import winsound
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
        self.speed(0)
        self.penup()
        self.color(color)
        self.goto(startx, starty)
        self.speed = 1

    def go_random(self):
        """Will send the object to a random location in screen"""
        x = random.randint(-240, 240)
        y = random.randint(-240, 240)
        self.goto(x, y)

    def is_collision(self, other):
        """Detect collision between two objects"""
        if other.xcor() - 20 <= self.xcor() <= other.xcor() + 20 and \
                other.ycor() - 20 <= self.ycor() <= other.ycor() + 20:
            return True
        else:
            return False

    def move(self):
        """Make objects of the class move around"""
        # forward() function moves the turtle forward
        self.forward(self.speed)
        angle = 70
        # Border detection
        if self.xcor() > 240:
            # Turn around when hit right border
            self.setx(240)
            # self.right(angle)
            self.setheading(random.randint(0, 360))
        if self.xcor() < -240:
            # Turn around when hit left border
            self.setx(-240)
            # self.right(angle)
            self.setheading(random.randint(0, 360))
        if self.ycor() > 240:
            # Turn around when hit top border
            self.sety(240)
            # self.right(angle)
            self.setheading(random.randint(0, 360))
        if self.ycor() < -240:
            # Turn around when hit bottom border
            self.sety(-240)
            # self.right(angle)
            self.setheading(random.randint(0, 360))


class SpaceShip(Sprite):
    def __init__(self, sprite_shape, color, startx, starty):
        Sprite.__init__(self, sprite_shape, color, startx, starty)
        self.speed = 4
        self.lives = 3

    def turn_left(self):
        """Turns the turtle by 45 degree to the left"""
        self.left(45)

    def turn_right(self):
        """Turns the turtle by 45 degree to the right"""
        self.right(45)

    def accelerate(self):
        """Accelerate the speed of the space ship"""
        self.speed += 1

    def decelerate(self):
        """Decelerate the speed of the space ship"""
        self.speed -= 1


class Enemy(Sprite):
    def __init__(self, sprite_shape, color, startx, starty):
        Sprite.__init__(self, sprite_shape, color, startx, starty)
        self.speed = 3
        self.setheading(random.randint(0, 360))
        # Will appear in random location
        self.go_random()


class Ally(Sprite):
    def __init__(self, sprite_shape, color, startx, starty):
        Sprite.__init__(self, sprite_shape, color, startx, starty)
        self.speed = 6
        self.setheading(random.randint(0, 360))
        # will appear in random location
        self.go_random()


class Missile(Sprite):
    def __init__(self, sprite_shape, color, startx, starty):
        Sprite.__init__(self, sprite_shape, color, startx, starty)
        self.speed = 20
        self.status = 'ready'
        # keep the missile out of screen until needed
        self.goto(-1000, 1000)
        self.shapesize(stretch_wid=0.3, stretch_len=0.4, outline=None)

    def fire(self):
        """Shoot the missile from the space ship"""
        if self.status == 'ready':
            # Get the missile to the position of the space ship
            self.goto(space_ship.xcor(), space_ship.ycor())
            # Set the direction of the missile to same direction of the space ship
            self.setheading(space_ship.heading())
            self.status = 'firing'

            # Play sound
            # os.system('afplay laser-gun.wav&') To play sound in mac
            # os.system('aplay laser-gun.wav&') To play sound in linux
            winsound.PlaySound('laser-gun.wav', winsound.SND_ASYNC)  # To play sound in Windows

    def move(self):
        """Will make the missile to move"""
        if self.status == 'firing':
            self.forward(self.speed)

        # Border Checking
        if self.xcor() > 250 or self.xcor() < -250 or \
                self.ycor() > 250 or self.ycor() < -250:
            self.goto(-1000, 1000)
            self.status = 'ready'


class Game:
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = 'playing'
        self.pen = turtle.Turtle()
        self.score_board = turtle.Turtle()
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

    def show_status(self):
        """Show the game status on the screen"""
        message = f'Score: {self.score}'
        self.score_board.speed(0)
        self.score_board.color('white')
        self.score_board.penup()
        self.score_board.goto(-250, 260)
        self.score_board.clear()
        self.score_board.write(message, font=('Arial', 14, 'normal'))


# Create the Game object
game = Game()
# Draw the border
game.draw_border()
# Show status
game.show_status()

# Create my sprites
space_ship = SpaceShip('triangle', 'white', 0, 0)
ally = Ally('square', 'blue', 0, 0)
enemy = Enemy('circle', 'red', 0, 0)
missile = Missile('triangle', 'yellow', 0, 0)

# Keyboard binding
window.listen()
window.onkeypress(space_ship.turn_left, 'Left')
window.onkeypress(space_ship.turn_right, 'Right')
window.onkeypress(space_ship.accelerate, 'Up')
window.onkeypress(space_ship.decelerate, 'Down')
window.onkeypress(missile.fire, 'space')

# Main game loop
while True:
    space_ship.move()
    ally.move()
    enemy.move()
    missile.move()

    # Collision check between space ship and enemy
    if space_ship.is_collision(enemy):
        enemy.go_random()
        # Lose point if you crash with enemy ship
        game.score -= 100
        game.show_status()

        # Play sound
        # os.system('afplay explosion.wav&') To play sound in mac
        # os.system('aplay explosion.wav&') To play sound in linux
        winsound.PlaySound('explosion.wav', winsound.SND_ASYNC)  # To play sound in Windows

    # Collision check between missile and enemy
    if missile.is_collision(enemy):
        enemy.go_random()
        missile.status = 'ready'
        missile.goto(-1000, 1000)
        # Shoot the enemy to gain point
        game.score += 100
        game.show_status()

        # Play sound
        # os.system('afplay explosion.wav&') To play sound in mac
        # os.system('aplay explosion.wav&') To play sound in linux
        winsound.PlaySound('explosion.wav', winsound.SND_ASYNC)  # To play sound in windows

    # Collision check between missile and ally
    if missile.is_collision(ally):
        ally.go_random()
        missile.status = 'ready'
        missile.goto(-1000, 1000)
        # You shoot your ally you lose point
        game.score -= 50
        game.show_status()

        # Play sound
        # os.system('afplay explosion.wav&') To play sound in mac
        # os.system('aplay explosion.wav&') To play sound in linux
        winsound.PlaySound('explosion.wav', winsound.SND_ASYNC)  # To play sound in windows
