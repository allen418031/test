num_tests = int(input())

for _ in range(num_tests):
    string = input()
    if string == string[::-1]:
        print("Yes")
    else:
        print("No")
