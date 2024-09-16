num_tests = int(input())

for _ in range(num_tests):
    n = int(input())
    m = int(input())
    arr = list(map(int, input().split()))
    
    num_dict = {}
    for i in range(n):
        complement = m - arr[i]
        if complement in num_dict:
            print(num_dict[complement], i)
            break
        else:
            num_dict[arr[i]] = i
