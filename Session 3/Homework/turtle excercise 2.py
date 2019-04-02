colors = ['red', 'blue', 'brown', 'yellow', 'grey']
j = 0
from turtle import *
while j <= 4 :
    color(colors[j],colors[j])
    begin_fill()
    for i in range(4):
        forward(150)
        left(90)
    end_fill()
    forward(150)
    j+=1
mainloop()