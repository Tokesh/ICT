s = str(input())
j = ""
for i in s:
    add_el = i.lower()
    if(add_el in 'aeouiy'): continue
    else:
        j += '.'
        j += add_el
print(j)