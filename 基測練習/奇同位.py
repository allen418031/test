k = int(input())

for _ in range(k):
    x = int(input())
    binary = bin(x)[2:]  # 將 x 轉換為二進制表示法，並去掉開頭的 '0b'
    count = binary.count('1')  # 計算二進制表示法中 '1' 的個數
    
    if count % 2 == 1:
        print(f"{x}: YES")
    else:
        print(f"{x}: NO")
