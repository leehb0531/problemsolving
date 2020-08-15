n = input()
space = " "
star = "*"
numOfSpace = int(n)-1
print("Type a number: "+ n)
for i in range(1,int(n)+1):
    numOfStar = 2*i-1
    print(space*numOfSpace+star*numOfStar)
    numOfSpace -= 1