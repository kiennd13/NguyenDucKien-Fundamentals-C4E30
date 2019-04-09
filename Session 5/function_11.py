test = []
rectangle = []
def is_inside(test,rectangle):
    if test[0] >= rectangle[0] and test[0] <= rectangle[0] + rectangle[2] and test[1] >= rectangle[1] and test[1] <= rectangle[1] + rectangle[3]:
        return "True"
    else:
        return "False"

rectangle = []
x = int(input("Nhập toạ độ x = "))
rectangle.append(x)
y = int(input("Nhập toạ độ y = "))
rectangle.append(y)
width = int(input("Chiều rộng : "))
rectangle.append(width)
height = int(input("Chiều dài : "))
rectangle.append(height)
test = []
t1 = int(input("Nhập toạ độ t1 = "))
test.append(t1)
t2 = int(input("Nhập toạ độ t2 = "))
test.append(t2)
result = is_inside(test,rectangle)
print(result)