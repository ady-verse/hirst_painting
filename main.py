# import colorgram
# colors = colorgram.extract('hirst.jpeg', 30)
# rgb=[]
# print(colors)
# for i in colors:
#     r=i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     newcolor=(r,g,b)
#     rgb.append(newcolor)
# print(rgb)
from turtle import Turtle, Screen
import random
screen = Screen()
screen.colormode(255)
timmy=Turtle()
timmy.speed("fastest")
color_list=[(198, 174, 118), (215, 224, 218), (222, 225, 229), (125, 36, 24), (162, 103, 57), (6, 55, 82), (185, 158, 53), (46, 34, 32), (108, 68, 85), (115, 161, 174), (23, 121, 171), (67, 152, 135), (76, 38, 47), (9, 66, 46), (88, 140, 59), (181, 96, 80), (129, 39, 42), (210, 201, 148), (142, 175, 161), (178, 155, 160), (178, 202, 184), (218, 181, 171), (31, 79, 62), (149, 116, 122), (210, 180, 184), (25, 75, 91), (171, 198, 208), (95, 139, 153)]

timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
NO=100
timmy.hideturtle()
for i in range(1, NO+1):
    timmy.dot(20,random.choice(color_list))
    timmy.forward(50)
    timmy.penup()
    if i%10==0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)
        timmy.penup()


screen.exitonclick()