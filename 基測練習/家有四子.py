n = int(input())  # 測試資料筆數

for _ in range(n):
    a, b, c, s = map(int, input().split())  # 讀取測試資料
    y = s - 20  # 小華的年齡
    z = y + b  # 小起的年齡
    w = z + c  # 小來的年齡
    print(y, z, w)  # 輸出結果
