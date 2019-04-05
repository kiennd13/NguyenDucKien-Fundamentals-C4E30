prices = {
    "banana" : 4,
    "apple" : 2,
    "orange" : 1.5,
    "pear" : 3
}
stock = {
    "banana" : 6,
    "apple" : 0,
    "orange" : 32,
    "pear" : 15
}
a = list(stock.values())
for k,v in prices.items():
    print(k)
    print("price:",v)
    for i in range(len(a)):
        print("stock:",a[i])
        a.pop(i)
        break
total = 0
float(total)
for m,n in prices.items():
    for x,y in stock.items():
        total += n*y
        stock.pop(x)
        break
print("Tổng tiền thu được sau khi bán hết số hoa quả là:",total)
