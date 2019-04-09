def input_list():
    ds=[]
    m=int(input("Nhập số phần tử: "))
    for v in range(m):
        so = int(input("Nhập số: "))
        ds.append(so)
    total=0    
    for i in range(len(ds)):
        total+=ds[i]
    print(total)
    print(total/len(ds))
    
input_list() #Gọi hàm
