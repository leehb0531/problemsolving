#별찍기-4

x = int(input())
for i in range(x, 0, -1):
    print(" "*(x-i) + "*" * i)