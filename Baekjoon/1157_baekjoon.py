#단어공부
#collections module의 Counter(string의 각 알파벳 빈도수 count) 사용
from collections import Counter
x = input()
x = x.upper()
cnt = Counter(x)
mode = cnt.most_common()
if len(mode) == 1:
    print(mode[0][0])
else:
    if mode[0][1] == mode[1][1]:
        print("?")
    else:
        print(mode[0][0])