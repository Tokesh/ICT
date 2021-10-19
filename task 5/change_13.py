vxod = int(input())
toonies = vxod // 200
vxod -= toonies * 200

loonies = vxod // 100
vxod -= loonies * 100

quarters = vxod // 25
vxod -= quarters * 25

dimes = vxod // 10
vxod -= dimes * 10

nickels = vxod // 5
vxod -= nickels * 5

pennies = vxod // 1
vxod -= pennies

print("You need to pay:")
print("Toonies:" , toonies)
print("Loonies:", loonies)
print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)
