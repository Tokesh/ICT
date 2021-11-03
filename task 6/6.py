s = str(input())
low_c = 0
upper_c = 0
for i in s:
    if(i.upper() == i): upper_c += 1
    else: low_c += 1
res = ""
if(upper_c > low_c):
    for i in s:
        res += i.upper()
else:
    for i in s:
        res += i.lower()
print(res)