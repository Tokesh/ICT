rows = int(input("Enter rows number: "))
for i in range(rows,-1,-1):
    for j in range(i, 0, -1):
        print(j , end= ' ')
    print()