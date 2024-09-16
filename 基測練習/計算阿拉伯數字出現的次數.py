# 讀取測試資料組數
test_cases = int(input())

# 進行每組測試
for _ in range(test_cases):
    # 讀取測試資料
    number = input().strip()

    # 初始化每個數字的出現次數為0
    counts = [0] * 10

    # 計算每個數字的出現次數
    for digit in number:
        counts[int(digit)] += 1

    # 輸出結果
    print(''.join(map(str, counts)))
