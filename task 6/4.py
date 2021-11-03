s = str(input())
maxi = -100000
cnt = 0
for i in range(len(s)-1):
    if(s[i] == s[i+1]):
        cnt += 1
        maxi = max(cnt,maxi)
    else: cnt = 0
if(maxi >= 6): print("YES")
else: print("NO")