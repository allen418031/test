import math

n = int(input())

for _ in range(n):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    
    side1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    side2 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    side3 = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    
    semi_perimeter = (side1 + side2 + side3) / 2
    area = math.sqrt(semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3))
    
    print("{:.3f}".format(area))
