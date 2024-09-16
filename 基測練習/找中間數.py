times = eval(input())

for i in range(times):
    a, b, c = map(int, input().split())  # 输入三个不同整数
    sorted_nums = sorted([a, b, c])  # 将三个数值排序
    middle_num = sorted_nums[1]  # 获取中间值
    print(middle_num)