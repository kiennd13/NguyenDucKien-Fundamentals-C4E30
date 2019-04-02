colors = ['red', 'blue', 'brown', 'yellow', 'grey']
j = 0
from turtle import *
while j <= 3:
    color(colors[j])
    for i in range(3):
        forward(150)
        left(120)
    j+=1    
    color(colors[j])
    for i in range(4):
        forward(150)
        left(90)
    j+=1    
    color(colors[j])
    for i in range(5):
        forward(150)
        left(72)
    j+=1
    color(colors[j])
    for i in range(6):
        forward(150)
        left(60)
    j+=1    
    color(colors[j])
    for i in range(7):
        forward(150)
        left(51.5)
mainloop()  