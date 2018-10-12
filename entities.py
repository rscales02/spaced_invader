# coding=utf-8
"""
creation Entity/Enemy/Player classes and their subsequent necessary functions
"""
import turtle
from config import Config


class Entity(turtle.Turtle):
    """
    create turtle class for both enemy and player
    """
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.distance = 15

    def set_distance(self, new_distance):
        """
        set distance variable
        """
        self.distance = new_distance

    def move_left(self):
        """
        move entities towards the left side of the screen
        """
        if self.heading() is not 180.0:
            self.setheading(180.0)
        if self.pos()[0] > Config.XMIN:
            self.forward(self.distance)

    def move_right(self):
        """
        move entities towards right of screen
        """
        if self.heading() is not 0.0:
            self.setheading(0.0)
        if self.pos()[0] < Config.XMAX:
            self.forward(self.distance)


class Player(Entity):
    """
    class for player(s), handle images
    """
    def __init__(self):
        Entity.__init__(self)
        self.color('blue')
        self.goto(0, -280)
        self.distance = 15
        self.shape(Config.IMAGE_DICT['baseship_b'])


class Enemy(Entity):
    """
    class for enemies, init handle images and place on screen
    """
    def __init__(self, xcord=0, ycord=0):
        Entity.__init__(self)
        self.color('red')
        self.goto(xcord, ycord)
        self.distance = 10
        self.shape(Config.IMAGE_DICT['saucer_1a'])
        self.speed(1)

    def move_vertical(self):
        """move down"""
        if self.heading() is not 90.0:
            self.seth(90.0)
        self.back(10)


