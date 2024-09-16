# 输入部分
test_cases = int(input())  # 输入的测试用例数量

for _ in range(test_cases):
    inputs = input().split()  # 拆分输入字符串
    num_grades = int(inputs[0])  # 雞蛋級數的數量
    prices = list(map(int, inputs[1:num_grades+1]))  # 雞蛋級數的價格列表
   
    quantities = list(map(int, inputs[num_grades+1:]))  # 不同級數雞蛋的數量列表
  
    # 计算总金额
    total_amount = 0
    for price, quantity in zip(prices, quantities):
        total_amount += price * quantity

    # 输出结果
    print(total_amount)
