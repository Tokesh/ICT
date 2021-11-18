arr = list(map(int,input().split()))
for i in arr:
    if(i > 300): break
    if(i > 120): continue
    if(i % 3 == 0): print(i)
