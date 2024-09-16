import math

num_cases = int(input())

for _ in range(num_cases):
    P, r, t = input().split()
    P = int(P)
    r = float(r)
    t = int(t)

    F = P * math.pow(1 + r/100/12, 12*t)
    F = round(F)

    print(F)
