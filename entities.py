import turtle
import time

IMAGE_DICT = {
    'baseship_a': 'images/gif_icons/baseshipa-0.gif',
    'baseship_b': 'images/gif_icons/baseshipb-0.gif',
    'mystery_a': 'images/gif_icons/mysterya.gif',
    'mystery_b': 'images/gif_icons/mysteryb.gif',
    'saucer_1a': 'images/gif_icons/saucer1a.gif',
    'saucer_1b': 'images/gif_icons/saucer1b.gif',
    'saucer_2a': 'images/gif_icons/saucer2a.gif',
    'saucer_2b': 'images/gif_icons/saucer2b.gif',
    'saucer_3a': 'images/gif_icons/saucer3a.gif',
    'saucer_3b': 'images/gif_icons/saucer3b.gif',
    'stars': 'images/gif_icons/stars.gif'
}

XMIN = -220
XMAX = 205
YMIN = -300
YMAX = 300


class Entity(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.distance = 15

    def move_left(self):
        if self.heading() is not 180.0:
            self.setheading(180.0)
        self.forward(self.distance)

    def move_right(self):
        if self.heading() is not 0.0:
            self.setheading(0.0)
        self.forward(self.distance)


class Player(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.color('blue')
        self.goto(0, -280)
        self.distance = 15
        self.shape(IMAGE_DICT['baseship_b'])


class Enemy(Entity):
    def __init__(self, xcord=0, ycord=0):
        Entity.__init__(self)
        self.color('red')
        self.goto(xcord, ycord)
        self.distance = 10
        self.looping = 0
        self.shape(IMAGE_DICT['saucer_1a'])

    def move_down(self):
        if self.heading() is not 90.0:
            self.seth(90.0)
        self.back(25)

    def loop(self):
        while self.looping < 100:
            time.sleep(10)
            if self.pos()[0] < XMIN or self.pos()[0] > XMAX:
                self.move_down()
                self.distance = -self.distance
            self.move_right()
            self.looping += 1
