# !/usr/bin/env python3 
# -*- coding: utf-8 -*- 
# @Author: Dwarika 
# @Env: python 3.6 
# @Github: https://github.com/Dwarkeshsahu/InfluenceCoding 

import turtle

s = turtle.getscreen()
turtle_obj = turtle.Turtle()

BODY_COLOR = 'red'
GLASS_COLOR = 'skyblue'
BACKPACK_COLOR = 'red'

def body():
	turtle_obj.pensize(20)
	turtle_obj.speed(1)
	turtle_obj.fillcolor(BODY_COLOR)
	turtle_obj.begin_fill()
	
	#right side of body 
	turtle_obj.right(90)
	turtle_obj.forward(50)
	turtle_obj.right(180)
	turtle_obj.circle(40,-180)
	turtle_obj.right(180)
	turtle_obj.forward(200)

	#head curve of body
	turtle_obj.right(180)
	turtle_obj.circle(100,-180)

	#left side of body
	turtle_obj.backward(20)
	turtle_obj.left(15)
	turtle_obj.circle(500,-20)
	turtle_obj.backward(20)
	turtle_obj.circle(40,-180)
	turtle_obj.left(7)
	turtle_obj.backward(50)

	#hip part 
	turtle_obj.up()
	turtle_obj.left(90)
	turtle_obj.forward(10)
	turtle_obj.right(90)
	turtle_obj.down()
	turtle_obj.right(240)
	turtle_obj.circle(50,-70)
	turtle_obj.end_fill()

def glass():
	turtle_obj.up()

	turtle_obj.right(230)
	turtle_obj.forward(100)
	turtle_obj.left(90)
	turtle_obj.forward(20)
	turtle_obj.right(90)

	turtle_obj.down()
	turtle_obj.fillcolor(GLASS_COLOR)
	turtle_obj.begin_fill()

	turtle_obj.right(150)
	turtle_obj.circle(90,-55)

	turtle_obj.right(180)
	turtle_obj.forward(1)
	turtle_obj.right(180)
	turtle_obj.circle(10,-65)
	turtle_obj.right(180)
	turtle_obj.forward(110)
	turtle_obj.right(180)

	turtle_obj.circle(50,-190)
	turtle_obj.right(170)
	turtle_obj.forward(80)

	turtle_obj.right(180)
	turtle_obj.circle(45,-30)

	turtle_obj.end_fill()


def backpack():
	turtle_obj.up()
	turtle_obj.right(60)
	turtle_obj.forward(100)
	turtle_obj.right(90)
	turtle_obj.forward(75)

	turtle_obj.fillcolor(BACKPACK_COLOR)
	turtle_obj.begin_fill()
	
	turtle_obj.down()
	turtle_obj.forward(30)
	turtle_obj.right(255)

	turtle_obj.circle(300,-30)
	turtle_obj.right(260)
	turtle_obj.forward(30)
	turtle_obj.end_fill()


body()
glass()
backpack()
