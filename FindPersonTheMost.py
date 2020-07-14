import sys

def sum1(list1,B):
    sum1 = 0
    for i in list1:
        sum1 += i*B
    return sum1

def sum2(list2,B,C):
    sum2 = 0
    for i in range(len(list2)-1):
        for _ in range(list2[i]):
            if list2[i] != 0 and list2[i+1] != 0:
                sum2 += B+C
                list2[i]-= 1
                list2[i+1] -= 1
    return sum2

def sum3(list3,B,C):
    sum3 = 0
    for i in range(len(list3)-2):
        for _ in range(list3[i]):
            if list3[i]!=0 and list3[i+1]!=0 and list3[i+2]!=0:
                sum3 += B+2*C
                list3[i] -= 1
                list3[i+1] -= 1
                list3[i+2] -= 1
    return sum3

condition = sys.stdin.readline().split()
B = int(condition[1])
C = int(condition[2])
lists = list(map(int,sys.stdin.readline().split()))
a = sum3(lists,B,C)
b = sum2(lists,B,C)
c = sum1(lists,B)
print(a+b+c)