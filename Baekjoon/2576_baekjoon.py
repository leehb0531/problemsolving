from sys import stdin
x_list = []
for _ in range(7):
    x_list.append(int(stdin.readline()))
y_list = []
a = 0
for i in x_list:
    if i % 2 == 1:
        a += i
        y_list.append(i)
y_sort = sorted(y_list)
if a == 0:
    print(-1)
else:
    print(a)
    print(y_sort[0])
