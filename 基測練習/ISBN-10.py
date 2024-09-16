num_tests = int(input())

for _ in range(num_tests):
    isbn = input()
    check_digit = sum(int(isbn[i]) * (i + 1) for i in range(9)) % 11
    if check_digit == 10:
        isbn += 'X'
    else:
        isbn += str(check_digit)
    print(isbn)
