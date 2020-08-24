#날짜 계산

fake = input().split()
fake = list(map(int,fake))
e=0
s=0
m=0
esm = []
real=0

while fake != esm:
    esm = []
    e += 1
    s += 1
    m += 1
    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1
    esm.append(e)
    esm.append(s)
    esm.append(m)
    real += 1
print(real)