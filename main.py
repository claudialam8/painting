import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 54)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_tuple = (r, g, b)
#     rgb_colors.append(rgb_tuple)
#
# print(rgb_colors)
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

# 10 x 10, circle 20 in size, 50 spaces apart

color_list = [(240, 241, 244), (230, 215, 101), (234, 246, 242), (154, 80, 38), (244, 231, 236), (207, 159, 105),
              (181, 175, 18), (108, 165, 210), (25, 91, 160), (106, 176, 124), (194, 91, 105), (13, 37, 97),
              (72, 43, 23), (50, 121, 23), (187, 133, 150), (94, 192, 47), (106, 32, 54), (195, 94, 75), (25, 97, 25),
              (100, 120, 169), (180, 206, 170), (250, 169, 173), (24, 53, 110), (251, 171, 163), (149, 191, 244),
              (104, 60, 18), (81, 30, 46), (132, 79, 90), (18, 75, 105), (91, 153, 156), (45, 49, 45), (104, 52, 26),
              (161, 202, 213), (213, 203, 31)]

tim.penup()
tim.speed("fastest")
tim.hideturtle()
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# print(tim.position())
for position in range(0, 11):
    tim.goto(-250, -250+50 * position)
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)






screen = t.Screen()
screen.exitonclick()
