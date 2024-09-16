num_cases = int(input())

for _ in range(num_cases):
    coins = int(input())
    
    candies = coins  # 初始糖果數量
    wrappers = candies  # 初始包裝紙數量
    
    while wrappers >= 3:
        exchanged_candies = wrappers // 3  # 換取的糖果數量
        candies += exchanged_candies
        wrappers = wrappers % 3 + exchanged_candies
    
    print(candies)
