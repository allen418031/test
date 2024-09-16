times = eval(input())

for i in range(times):
    num = input()  # 輸入一個數值
    num_str = str(num)
    is_gap = True

    for i in range(len(num_str) - 1):
        if num_str[i] == num_str[i+1]:
            is_gap = False
            break

    if len(set(num_str)) == 2 and is_gap:
        print("Yes")
    else:
        print("No")