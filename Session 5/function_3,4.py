# from turtle import *
# for i in range(4):
#     forward(200)
#     left(90)
# mainloop()
from turtle import *
def draw_square(length,colors):
    color(colors)
    for _ in range (4):
        forward(length)
        left(90)
    mainloop()    
x = int(input("Length = "))
y = str(input("Color : "))
draw_square(x,y)
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

