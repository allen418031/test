N = int(input())

for _ in range(N):
    lotto_numbers = list(map(int, input().split()))

    if len(lotto_numbers) != 7:  # 樂透號碼必須有 7 個數字
        print("No")
    elif any(num < 1 or num > 49 for num in lotto_numbers):  # 號碼必須介於 1~49 之間
        print("No")
    elif len(set(lotto_numbers)) != 7:  # 號碼不能重複
        print("No")
    else:
        print("Yes")
