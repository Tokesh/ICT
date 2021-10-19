import math
r = 6371.01
x1 = math.radians(float(input()))
y1 = math.radians(float(input()))
x2 = math.radians(float(input()))
y2 = math.radians(float(input()))
d = r * math.acos(math.sin(y1)*math.sin(y2) + math.cos(y1)*math.cos(y2)*math.cos(x1-x2))
print(d, "km")