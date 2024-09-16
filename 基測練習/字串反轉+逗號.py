times = eval(input())

for i in range(times):
    string = input().strip()
    print(string)
    reverse= ",".join(string[::-1])

    print(reverse)