num_rows = int(input())

for _ in range(num_rows):
    hair_lengths = list(map(int, input().split()))
    sorted_hair_lengths = sorted(hair_lengths)  # 按照頭髮長度由小到大排序
    
    if hair_lengths == sorted_hair_lengths:
        print("YES")
    else:
        print("NO")
