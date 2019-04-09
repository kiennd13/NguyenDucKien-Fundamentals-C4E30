from turtle import *
def draw_star(x,y,length):
    up()
    setposition(x,y)
    down()
    for _ in range(5):
        left(144)
        forward(length)
    mainloop()
length = int(input("Length = "))
x = int(input("Position 1: "))
y = int(input("Position 2: "))
draw_star(x,y,length)
speed(0.3)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
