num = int(input("Enter number of terms: "))
a = 0
b = 1
cnt = 0
print("Fibonacci sequence:")
while(num != 0): 
    print(a, end=' ')
    a,b = b, a+b
    num -= 1
    
