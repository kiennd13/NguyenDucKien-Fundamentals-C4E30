our_items = ["T-shirt","Sweater"]
n = input("Welcome to our shop, what do you want (C, R, U, D)? ")
if n == "R" :
    for our_items in our_items:
        print(our_items,end=' ')
if n == "C" :
    x = input("Enter new item: ")
    our_items.append(x)
    for our_items in our_items:
        print(our_items,end=' ')
if n == "U" :
    x = int(input("Update position? "))
    y = input("New item: ") 
    our_items[x-1] = y 
    for our_items in our_items:
        print(our_items,end=' ')
if n == "D" :
    x = int(input("Delete position? "))
    our_items.pop(x-1)
    for our_items in our_items:
        print(our_items,end=' ')