#모음의 개수

while True:
    x = input()
    if x !="#":
        Al = "aeiouAEIOU"
        a = 0
        for i in Al:
            n = x.count(i)
            a+=n
        print(a)
    else:
        break