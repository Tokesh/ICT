k = int(input())
s = str(input())
cnt = 0
res = 0
for i in s:
    if(i == 'x'):
        cnt += 1
    else: 
        if(cnt >= 3):
            res += cnt-3+1
        cnt = 0

if(cnt >= 3):
    res += cnt-3+1
print(res)
    