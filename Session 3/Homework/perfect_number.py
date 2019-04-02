pn=[]
n = 1
while n <10000 :
    ds=[]
    for i in range(1,n):
        if n % i == 0 :
            ds.append(i)
    t = 0
    for i in range(len(ds)):
        t+= ds[i]
    if t == n:
        pn.append(t)
    n+=1
print(pn)     
    