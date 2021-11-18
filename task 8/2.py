nums = int(input("Enter number: "))
sumi = 0
for i in range(nums+1):
    sumi += i
print(f"Sum of first %d numbers is:" % nums, sumi)
print(f"Average of %d numbers is:" % nums, sumi / nums)