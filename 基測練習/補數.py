# 讀取測試資料筆數
num_cases = int(input())

for _ in range(num_cases):
    binary = input()
    
    # 轉換成反碼
    complement = ''.join('0' if bit == '1' else '1' for bit in binary)
    
    # 加 1
    carry = 1
    result = ''
    for bit in complement[::-1]:
        if bit == '0' and carry == 1:
            result += '1'
            carry = 0
        elif bit == '1' and carry == 1:
            result += '0'
        else:
            result += bit
    
    twos_complement = result[::-1]
    print(twos_complement)
