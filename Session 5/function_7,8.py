def remove_dollar_sign(s): 
    return s.replace("$","")
m = str(input("Nhập chuỗi : "))
t=remove_dollar_sign(m)
print(t)
string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")