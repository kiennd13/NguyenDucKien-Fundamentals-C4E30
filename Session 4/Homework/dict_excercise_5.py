print("Answer the following algebra question: ")
print("If x=8, then what is the value of 4(x+3)?")
quiz={
    1: 35,
    2: 36,
    3: 40,
    4: 44
}
for k,v in quiz.items():
    print(str(k)+'.',v)
n = int(input("Your choice: "))
count = 0
if n != 4:
    print(":(")
else:
    print("Bingo") 
    count += 1
print("Estimate this answer(exact calculation not needed: ")
print("Jack scored these mark in 5 math test: 49,81,72,66,52. What is the mean?")
quiz_2 = {
    1: "About 55",
    2: "About 65",
    3: "About 75",
    4: "About 85"
}
for k,v in quiz_2.items():
    print(str(k)+'.',v)
n = int(input("Your choice: "))
if n != 2:
    print(":(")
else:
    print("Bingo") 
    count += 1
print("You correctly answer",count,"out of 2 questions")