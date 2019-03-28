weight = float(input("Nhập cân nặng(kg) : "))
height = float(input("Nhập chiều cao(cm) :"))
x = weight / ((height/100)**2)
BMI = print("BMI = ",round(x,2))
if x < 16 :
    print("Severely underweight")
elif x < 18.5 :
    print("Underweight")
elif x < 25 :
    print("Normal")
elif x < 30 :
    print("Overweight")
else :
    print("Obese")
