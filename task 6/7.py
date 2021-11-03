i = int(input())
s = str(input())
j = ""
for i in s:
    j += i.lower()
if(26 == len(set(j))): print("YES")
else: print("NO")