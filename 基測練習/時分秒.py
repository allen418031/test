num_tests = int(input())

for _ in range(num_tests):
    seconds = int(input())
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    time_str = "%02d:%02d:%02d" % (hours, minutes, seconds)
    print(time_str)
