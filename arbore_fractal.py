#! /usr/bin/python3
#+ coding: utf-8
#------------------------------------------------------------------------------------------------
#+ Autor:	Ran#
#+ Creado:	28/06/2021 19:40:28
#+ Editado:	10/08/2021 14:36:02
#------------------------------------------------------------------------------------------------

from turtle import *

def tree(size, levels, angle):
    if levels == 0:
        color('green')
        dot(size)
        color('black')
        return

    forward(size)
    right(angle)

    tree(size*0.8, levels-1, angle)

    left(angle*2)

    tree(size*0.8, levels-1, angle)

    right(angle)
    backward(size)

def snowflake_side(length, levels):
    if levels == 0:
        forward(length)
        return

    length /= 3.0
    snowflake_side(length, levels-1)
    left(60)
    snowflake_side(length, levels-1)
    right(120)
    snowflake_side(length, levels-1)
    left(60)
    snowflake_side(length, levels-1)

def create_snowflake(sides, length):
    colors = ['green', 'blue', 'red', 'yellow', 'orange']
    for i in range(sides):
        color(colors[i])
        snowflake_side(length, sides)
        right(360 / sides)

if __name__ == '__main__':
    shape('turtle')
    speed(0)

    left(90)
    tree(70, 5, 30)
    left(180)
    create_snowflake(3, 200)

    mainloop()

#------------------------------------------------------------------------------------------------
