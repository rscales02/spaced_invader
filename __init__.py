import turtle
import entities

wn = turtle.Screen()
wn.setup(480, 640)

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

wn.bgpic(IMAGE_DICT['stars'])

for key in IMAGE_DICT:
    wn.addshape(IMAGE_DICT[key])


def draw_border():
    border_turtle = turtle.Turtle()
    border_turtle.hideturtle()
    border_turtle.penup()
    border_turtle.setx(-235)
    border_turtle.sety(317)
    border_turtle.pensize(5)
    border_turtle.pendown()
    for i in range(2):
        border_turtle.forward(463)
        border_turtle.right(90)
        border_turtle.forward(626)
        border_turtle.right(90)
    border_turtle.penup()


draw_border()
player = entities.Player()
enemies = []
xcord = -200
ycord = 200
for i in range(24):
    enemies.append(entities.Enemy(xcord, ycord))
    xcord += 75
    if xcord > 200:
        xcord = -200
        ycord -= 50


player.shape(IMAGE_DICT['baseship_a'])

for enemy in enemies:
    enemy.shape(IMAGE_DICT['mystery_a'])


wn.onkeypress(player.move_left, "Left")
wn.onkeypress(player.move_right, "Right")
wn.listen(xdummy=None, ydummy=None)
wn.mainloop()
