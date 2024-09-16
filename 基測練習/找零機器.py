while True:
    money = int(input())
    if money == 0:
        break
    
    # 計算各個銅板數
    fifty = money // 50
    money %= 50
    
    ten = money // 10
    money %= 10
    
    five = money // 5
    money %= 5
    
    one = money
    
    print(f"{fifty} {ten} {five} {one}")
