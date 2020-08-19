## 몇자리 수 인지 구하는 함수
def nofn(n):
    many = []
    num = str(n)
    for i in num:
        many.append(i)
    return len(many)

##숫자의 각 자리수를 요소라 가지는 list로 바꾼다
def each(a):
    new = []
    snum = str(a)
    for i in snum:
        new.append(int(i))
    return new

x = int(input()) #x는 자연수 0>
total = 99
if x<100: #두자리 숫자까지는 무조건 한수 이므로 
    print(x)
else: #100부터는
    for i in range(100, x + 1): #input까지
        p = each(i)
        sub = []
        for j in range(1, nofn(i)):
            sub.append(p[j]-p[j-1]) #요소들의 차를 요소로 갖는 sub list
        if sub.count(sub[0]) == len(sub): #같은 요소들의 개수가 sub list의 size와 같으면 한수
            total += 1
    print(total)