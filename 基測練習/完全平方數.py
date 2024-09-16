num_tests = int(input())

for _ in range(num_tests):
    a, b = map(int, input().split())
    
    # 找出 a 到 b 之間的完全平方數，並計算總和
    total = sum([i*i for i in range(int(a**0.5)+1, int(b**0.5)+1)])
    
    print(total)
