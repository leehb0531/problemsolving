#크로아티아 알파벳

special = ["c=","c-","dz=","d-","lj","nj","s=","z="]
x = input() # string
a = [] # list
for i in x:
    a.append(i)
total = 0
for i in special:
    if i in x:
        if x.count(i)>1:
            total += x.count(i)
            x = x.replace(i, " ")
        else:
            total += 1
            x = x.replace(i, " ")
print(len(x)+total-x.count(" "))
