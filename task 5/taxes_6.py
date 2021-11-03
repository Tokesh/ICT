array_of_food_prices = list(map(int,input().split()))
# or if they give us N numbers
# we can do n=int(input())
# for i in range(n)
#   x = int(input())
sumi = 0
for i in array_of_food_prices:
    sumi += i
tips = float(sumi) * 0.18
local_tax = sumi * 0.12
print("Sum of local tax", "%.2f" % float(local_tax))
print("Sum of tips", "%.2f" % float(tips))
print("Total price", "%.2f" % float(tips+local_tax+sumi))