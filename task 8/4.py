import math
def prime_check(num):
    for i in range(2, int(math.sqrt(num)+1)):
        if(num % i == 0): return False
    return True

start_num = int(input("Enter starting number: "))
end_num = int(input("Enter ending number: "))
for i in range(start_num, end_num + 1):
    if(prime_check(i)): print(i)
