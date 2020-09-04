#곱셈

x = int(input())
y = input()
answer = []

for i in str(y)[::-1]:
    answer.append(x*int(i))
for i in range(len(str(y))):
    print(answer[i])
print(x*int(y))
