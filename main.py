import turtle
import entities
import game_play
from config import Config

wn = turtle.Screen()
wn.setup(480, 640)
wn.bgpic(Config.IMAGE_DICT['stars'])

for key in Config.IMAGE_DICT:
    wn.addshape(Config.IMAGE_DICT[key])

entity_dict = game_play.create_entity_dict()
player = entity_dict['player']


wn.onkeypress(player.move_left, "Left")
wn.onkeypress(player.move_right, "Right")
wn.listen(xdummy=None, ydummy=None)


game_play.game_loop(entity_dict)


wn.mainloop()
