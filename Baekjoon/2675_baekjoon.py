#문자열 반복

T = int(input())
want = []
for i in range(T):
    case = input().split()
    nR = int(case[0])
    newlist = ""
    for new in case[1]:
        newlist += new*nR
    want.append(newlist)
for num in want:
    print(num)