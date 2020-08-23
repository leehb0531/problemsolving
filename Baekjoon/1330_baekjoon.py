#두수 비교하기

x,y = input().split()
if int(x) < int(y):
    print('<')
elif int(x) > int(y):
    print('>')
else:
    print('==')