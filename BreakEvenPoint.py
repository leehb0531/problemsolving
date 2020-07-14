import sys

x= sys.stdin.readline().split()
A = int(x[0])
B = int(x[1])
C = int(x[2])
amount = 1
income = amount * C
cost = A+B*amount
difference = cost-income
no = 0
if(income > cost):
    print(1)
else:
    while(cost >= income):
        amount += 1
        income = amount * C
        cost = A+B*amount
        if(amount>1 and difference < cost-income):
            no = -1
            break
        difference = cost-income
    if(no == -1):
        print(no)
    else:
        print(amount)