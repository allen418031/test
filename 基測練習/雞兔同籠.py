k = int(input())

for _ in range(k):
    n, f = map(int, input().split())

    # 計算兔子數量和雞的數量
    r = (f - 2 * n) / 2
    c = n - r

    # 判斷計算是否有錯誤
    if r < 0 or c < 0 or r % 1 != 0 or c % 1 != 0:
        print("False")
    else:
        print(int(r), int(c))
