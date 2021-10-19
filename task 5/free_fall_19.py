import math
height = float(input())
a = 9.8
vi = 0
vf = vi + 2 * a * height
print("%.2f" % vf)
velocity = math.sqrt(2 * a * height)
print("%.2f" % velocity)