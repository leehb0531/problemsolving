#음계

group = input().split()
Sort = sorted(group)
re_sort = sorted(group, reverse=True)
if group == Sort:
    print('ascending')
elif group == re_sort:
    print('descending')
else:
    print('mixed')