k = int(input())  # 測試資料筆數

for _ in range(k):
    a, b = map(int, input().split())  # 讀取測試資料

    n = 0
    while a ** n <= b:
        n += 1

    print(n - 1)  # 輸出結果
