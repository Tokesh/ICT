s = str(input())
f_cnt = 0
s_cnt = 0
t_cnt = 0
for i in s:
    if(i =='1'): f_cnt += 1
    elif(i == '2'): s_cnt += 1
    elif(i == '3'): t_cnt += 1
res = ""
while(f_cnt != 0 or s_cnt != 0 or t_cnt != 0):
    if(f_cnt != 0):
        res += '1'
        f_cnt -= 1
    elif(s_cnt != 0):
        res += '2'
        s_cnt -= 1
    elif(t_cnt != 0):
        res += '3'
        t_cnt -= 1
    if(f_cnt != 0 or s_cnt != 0 or t_cnt != 0):
        res += '+'
print(res)
