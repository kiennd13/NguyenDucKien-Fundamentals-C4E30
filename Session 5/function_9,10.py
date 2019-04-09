av = []
def get_even_list(av):
    new_ds = []
    for i in range(len(av)):
        if av[i] % 2 == 0:
            k = av[i]
            new_ds.append(k)
    return new_ds
ds=[]
n = int(input("Nhập số phần tử: "))
for i in range (n):
   i = int(input("Nhập phần tử: "))
   ds.append(i)
t=get_even_list(ds)
print(t)
even_list = get_even_list([1, 2, 5, 9, -10, 6])
if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
