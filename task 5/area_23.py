import math
side = float(input())
number_sides = int(input())
area = number_sides * ((side *side) / 4*math.tan(math.pi/number_sides))
print(area)