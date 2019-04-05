y = 0
tien_nam_sau = 21
whisle True :
    tien_nam_sau = tien_nam_sau + tien_nam_sau*0.065
    tien_nam_sau = tien_nam_sau
    y = y+1
    if y == 10 :
        print("Sau 9 năm,ta có:",round(tien_nam_sau,2)) 
    if tien_nam_sau >= 1200:
        print("Thời gian cần tối thiểu để có 1 tỷ 2 là :",y,"năm")
        print("Lúc đó ta có : ", round(tien_nam_sau,2))
        break



    
