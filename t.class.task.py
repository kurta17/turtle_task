import turtle as t
import random
from pprint import pprint

# # TASK 1

# def drow_square():
#     for i in range(4):
#         t.width(10)
#         t.color("blue")
#         t.forward(100)
#         t.left(90)
       
           
# drow_square()
# t.Screen.mainloop() 


# #TASK 2

# def draw_dotted():
#     t.pencolor("red")
#     while True:
#         t.penup()
#         t.forward(10)
#         t.pendown()
#         t.forward(10)
# draw_dotted()


# #TASK 3
# import turtle as t
# import random
# def make_figures():
#     col = ["red", "blue", "black"]
#     t.width(10)
#     t.speed(5)   
    
#     for i in range(3,10):
#         ran_col = random.choice(col)
#         t.color(ran_col)
#         angle = int(360 // i)
#         for x in range(i):
#             t.forward(100)
#             t.right(angle)
          
        

# make_figures()

# #TASK 4
# import time
# def ran_walk():
    
#     angle = [90, 270]
#     for i in range(100):
        
#         while i < 100:
#             color = [random.random(), random.random(),random.random()]
#             t.width(10)
#             t.pencolor(color)
#             ran = float(random.choice(angle))
#             t.forward(50)
#             t.left(ran)

# ran_walk()   
    

# #TASK 5
# def make_circle(n):
#     t.speed(50)
#     for i in range(n):
#         color = [random.random(), random.random(),random.random()]
#         t.pencolor(color)
#         t.circle(50)
#         t.right(360 // n)


# make_circle(60)

#TASK cologram


import colorgram
import turtle as t
from pprint import pprint
import turtle as t
import colorgram

colors = colorgram.extract('photo.jpg', 25)


screen = t.Screen()
screen.setup(width=800, height=700)
screen.bgcolor("white")

my_turtle = t.Turtle()


my_turtle.penup()
my_turtle.speed("fastest")


circles_per_row = 5
circle_spacing = 150
color_rgb = []

# for i in range(25):
#     rgb_list = []
#     item1 = colors[i].rgb.r
#     item2 = colors[i].rgb.g
#     item3 = colors[i].rgb.b
#     rgb_list.append(item1)
#     rgb_list.append(item2)
#     rgb_list.append(item3)
#     color_rgb.append(rgb_list)

# pprint(color_rgb)

for row in range(5):
    for _ in range(5):
        color_index = random.randint(1,24)
        r = colors[color_index].rgb.r / 255.0
        g = colors[color_index].rgb.g / 255.0
        b = colors[color_index].rgb.b / 255.0
        my_turtle.fillcolor(r, g, b)
        my_turtle.penup()
        my_turtle.goto(-360 + _ * circle_spacing, 260 - row * circle_spacing)
        my_turtle.pendown()
        my_turtle.begin_fill()
        my_turtle.circle(30)  
        my_turtle.end_fill()


my_turtle.hideturtle()
screen.exitonclick()
