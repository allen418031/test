from datetime import datetime

num_tests = int(input())

for _ in range(num_tests):
    year, month, day = map(int, input().split())
    date_str = f"{year}-{month:02d}-{day:02d}"
    date = datetime.strptime(date_str, "%Y-%m-%d")
    weekday = date.strftime("%w")
    print(weekday)
