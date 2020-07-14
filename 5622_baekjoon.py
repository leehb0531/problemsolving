def returnNumber(aString):
  aS = aString
  if aS in "ABC":
    return 2
  elif aS in "DEF":
    return 3
  elif aS in "GHI":
    return 4
  elif aS in "JKL":
    return 5
  elif aS in "MNO":
    return 6
  elif aS in "PQRS":
    return 7
  elif aS in "TUV":
    return 8
  elif aS in "WXYZ":
    return 9
  elif aS in " ":
    return 1
  else:
    return 10


x = input()
nList=[]
for i in x:
  nList.append(returnNumber(i))
howLong = map(lambda x: x+1 , nList)
result = sum(howLong)
print(result)