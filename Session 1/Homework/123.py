# a = 5
# b = 7
# print (a-b)
# a = a + b
# b = a - b
# a = a - b
# print (a,b)


from turtle import *
shape('turtle')
speed(0.1)
for i in range(100):
    forward(200)
    left(90)
    forward(200)
    left(90)
    forward(200)
    left(90)
    forward(200)
    left(5)

mainloop()
