#별찍기-2

x=int(input())
for i in range(x,0,-1):
    print(" "*(i-1)+"*"*(x-i+1))