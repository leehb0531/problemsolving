#럭비 클럽

while True:
    x = input().split()
    if x[0] == '#':
        break
    elif int(x[1]) > 17 or int(x[2]) >= 80:
        print('%s %s'%(x[0],'Senior'))
    else:
        print('%s %s' % (x[0], 'Junior'))