salary = int(input())
year = float(input())
bonus = 0
if(year > 5): bonus = (salary * 1.05) - salary
print(int(bonus))