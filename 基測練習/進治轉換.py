num_cases = int(input())

for _ in range(num_cases):
    octal_num = input()
    if octal_num == "8":
        print(10)
    else:
        decimal_num = int(octal_num, 8)
        
        quaternary_num = ""
        if decimal_num == 0:
            quaternary_num = "0"
        
        while decimal_num > 0:
            remainder = decimal_num % 4
            quaternary_num = str(remainder) + quaternary_num
            decimal_num //= 4
        
        print(quaternary_num)
