n = str(input("Nhập chuỗi : "))
counts = {}
for i in n:
    counts[i] = counts.get(i,0) + 1
a = list(counts.items())
a.sort()
for i,j in a:
    print(i,j)