k = int(input())
s = str(input())
z = 0
e = 0
r = 0 
o = 0
n = 0
for i in s:
    if(i == 'z'): z += 1
    elif(i == 'e'): e += 1
    elif(i == 'r'): r += 1
    elif(i == 'o'): o += 1
    elif(i == 'n'): n += 1
one = min(o,n,e)
temp = min(o,n,e)
o -= temp
n -= temp
e -= temp
zero = min(z,e,r,o)
j =""
while(one != 0 or zero != 0):
    if(one != 0):
        j += '1'
        one -= 1
    else: 
        j += '0'
        zero -= 1
for i in j:
    print(i, end= ' ')