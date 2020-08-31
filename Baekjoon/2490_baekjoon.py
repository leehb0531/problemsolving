#윷놀이

for _ in range(3):
    x = input().split()
    y = x.count("0")
    if y == 1:
        print("A")
    elif y == 2:
        print("B")
    elif y == 3:
        print("C")
    elif y == 4:
        print("D")
    else:
        print("E")