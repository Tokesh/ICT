z = int(input())
s = str(input())
a_cnt = 0
d_cnt = 0
for i in s:
    if(i == 'A'): a_cnt += 1
    else: d_cnt += 1
if(a_cnt > d_cnt):
    print("Anton")
elif(a_cnt < d_cnt):
    print("Danik")
else: print("Friendship")