
import sys

total = int(sys.stdin.readline())
result = 0
userL= set()
userL.add("ENTER")
for i in range(total):
  user= sys.stdin.readline().strip()
  if user == "ENTER":
    result+=len(userL)-1
    # print(result)
    userL.clear()
    userL.add("ENTER") 
  userL = userL | {user} # "|"이게 시간을 엄청 많이 먹나??? 
  # print(userL)

result += len(userL)-1

print(result)
#####


######
# userL = set()
# result = 0
# for _ in range(total):
#   user = sys.stdin.readline().strip()
#   if user == "ENTER":
#     result += len(userL)
#     userL.clear()
#   elif user != "ENTER" and user not in userL:
#     userL.add(user)
# result += len(userL)
# print(result)