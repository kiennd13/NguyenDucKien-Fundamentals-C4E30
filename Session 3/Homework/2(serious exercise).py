sheep_size = [5,7,300,90,24,50,75]
print("Hello, i'm Kien and these are my ship sizes")
print(sheep_size)
for n in range (4):
    print("Month",n+1,":")
    print("One month has passed,now here is my flock:")
    for i in range (len(sheep_size)):
        sheep_size[i] = sheep_size[i] + 50
    print(sheep_size)
    max = sheep_size[0]
    j = 0
    for i in range (len(sheep_size)):
        if sheep_size[i] > max:
            max = sheep_size[i]
            j = i
    print("Now my biggest sheep has size",max,"let's shear it")
    sheep_size[j] = 8
    print("After shearing, here is my flock:")
    print(sheep_size)
t = 0
for i in range (len(sheep_size)):
    t += sheep_size[i]  
print("My flock has size total: ",t)
print("I would get",t,"* 2$ = ",t*2,"$" )
