import turtle


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
        self.goto(0, -250)
        self.distance = 15


class Enemy(Entity):
    def __init__(self, xcord=0, ycord=0):
        Entity.__init__(self)
        self.color('red')
        self.goto(xcord, ycord)

    def move_down(self):
        if self.heading() is not 90.0:
            self.seth(90.0)
        self.back()
