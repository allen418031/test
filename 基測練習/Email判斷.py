while True:
    email = input()

    if email == '0':
        break

    at_index = email.find('@')
    dot_index = email.find('.')

    if at_index != -1 and dot_index != -1 and at_index < dot_index and at_index != 0:
        print(True)
    else:
        print(False)
