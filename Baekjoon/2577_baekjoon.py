# 숫자의 개수

x = int(input())
y = int(input())
z = int(input())
a = str(x*y*z)
for i in range(10):
    b = a.count(str(i))
    print(b)