# coding=utf-8
"""
game play physics
"""
import entities
import turtle
from config import Config


def create_entity_dict():
    """
    create dictionary of entities
    :return: dictionary of entities
    """
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
    return {'player': player, 'enemies': enemies}


def game_loop(entity_dict):
    """
    loop through the game logic
    :param entity_dict: expects dictionary of entity objects
    """
    player = entity_dict['player']
    enemies = entity_dict['enemies']
    for enemy in enemies:
        enemy_pos = [enemy.pos()]
        # if len(list(filter(lambda x: x + enemy.distance < Config["XMIN"] or x + enemy.distance > Config['XMAX'], enemy_pos))):
        #     enemy.set_distance(-enemy.distance)
        enemy.move_right()

    turtle.ontimer(game_loop(entity_dict), 10)
