num_tests = int(input())

for i in range(num_tests):
    n = int(input())

    if n == 0:
        print("0")
    else:
        result = ""
        while n != 0:
            remainder = n % (-2)
            n //= (-2)
            
            if remainder < 0:
                remainder += 2
                n += 1
                
            result = str(remainder) + result
            
        print(result)
