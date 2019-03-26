a = int(input('cạnh 1 :'))
b = int(input('cạnh 2 :'))
c = int(input('cạnh 3 :'))
p = (a + b + c)/2
print("chu vi tam giác =", p)
S = p*(p-a)*(p-b)*(p-c)**0.5
print('Diện tích tam giác =', S)