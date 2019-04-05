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
if n != 4:
    print(":(")
else:
    print("Bingo") 