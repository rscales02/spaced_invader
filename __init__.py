import turtle
import entities
import time

wn = turtle.Screen()
wn.setup(480, 640)




wn.bgpic(entities.IMAGE_DICT['stars'])

for key in entities.IMAGE_DICT:
    wn.addshape(entities.IMAGE_DICT[key])

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


wn.onkeypress(player.move_left, "Left")
wn.onkeypress(player.move_right, "Right")
wn.listen(xdummy=None, ydummy=None)

# time.sleep(10)
# for enemy in enemies:
#     enemy.move_right()
wn.mainloop()
