T = int(input())

for _ in range(T):
    sentence = input()
    words = sentence.split()
    count = 0
    
    for word in words:
        if len(word) >= 10 and word.isalpha():
            count += 1
    
    print(count)
