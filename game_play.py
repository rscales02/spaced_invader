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
    x_cord = -200
    y_cord = 200
    for i in range(24):
        enemies.append(entities.Enemy(x_cord, y_cord))
        x_cord += 75
        if x_cord > 200:
            x_cord = -200
            y_cord -= 50
    return {'player': player, 'enemies': enemies}


def draw_cover():
    """
    insert cover for fighter
    :return:
    """
    x_min = Config.XMIN + 30
    y_min = Config.YMIN + 100

    for i in range(3):
        t = turtle.Turtle()
        t.hideturtle()
        t.fillcolor('green')
        t.penup()
        t.goto(x_min, y_min)
        t.begin_fill()
        t.begin_poly()
        t.pd()
        for i in range(2):
            t.forward(90)
            t.left(90)
            t.forward(45)
            t.left(90)
        t.end_poly()
        t.end_fill()
        x_min += 150


def game_loop(entity_dict):
    """
    loop through the game logic
    :param entity_dict: expects dictionary of entity objects
    """
    enemies = entity_dict['enemies']
    next_enemy_pos = list(map(lambda x: x.pos()[0] + x.distance, enemies))
    if len(list(filter(lambda x: x < Config.XMIN or x > Config.XMAX, next_enemy_pos))):
        for enemy in enemies:
            enemy.distance = -enemy.distance
            enemy.move_vertical()
            if enemy.speed() < 10:
                enemy.speed(enemy.speed() + 1)
    for enemy in enemies:
        enemy.move_right()

    turtle.ontimer(game_loop(entity_dict), 10)
