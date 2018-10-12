# coding=utf-8
"""
main file for space invaders, bringing the pieces together
"""

import turtle
import game_play
from config import Config

wn = turtle.Screen()
wn.setup(Config.WN_WIDTH, Config.WN_HEIGHT)
wn.bgpic(Config.IMAGE_DICT['stars'])

for key in Config.IMAGE_DICT:
    wn.addshape(Config.IMAGE_DICT[key])

entity_dict = game_play.create_entity_dict()
player = entity_dict['player']

game_play.draw_cover()

wn.onkeypress(player.move_left, "Left")
wn.onkeypress(player.move_right, "Right")
wn.onkeypress(turtle.bye, "Escape")

wn.listen(xdummy=None, ydummy=None)

game_play.game_loop(entity_dict)

wn.mainloop()
