a=[]
for x in range(1,6):
    for y in range(1,6):
        for z in range(1,6):
                for t in range(1,6):
                        for q in range(1,6):   
                            if x!=y and x!=z and x!=t and x!=q and y!=z and y!=t and y!=q and z!=t and z!=q and t!=q :    
                                a.append(str(x)+str(y)+str(z)+str(t)+str(q))
a = list(map(int, a))
print("Các hoán vị của 12345 : ")
for a in a:
        print(a,end=' ')