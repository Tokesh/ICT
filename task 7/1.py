prices = {'L':25, 'M':20, 'S':15}
size = str(input())
add_pepperoni = str(input())
extra_cheese = str(input())
total = prices[size]
if(add_pepperoni == 'Y'):
    if(size == 'S'): total += 2
    else: total += 3
if(extra_cheese == 'Y'): total += 1
print("Your final bill is: $",total, sep ='')