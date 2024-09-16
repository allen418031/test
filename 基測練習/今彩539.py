winning_numbers = input().split()
k = int(input())

for _ in range(k):
    guess_numbers = input().split()
    match_count = 0
    
    for num in guess_numbers:
        if num in winning_numbers:
            match_count += 1
    
    print(match_count)
