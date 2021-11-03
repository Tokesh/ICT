s = str(input())
cnt = 0
for i in range(1,len(s)):
    if(s[i].upper() == s[i]): cnt += 1
if(len(s) == 1 or cnt == len(s)-1):
    res = ""
    for i in range(len(s)):
        if(s[i].upper() == s[i]): res += s[i].lower()
        else: res += s[i].upper()
    print(res)
else: print(s)