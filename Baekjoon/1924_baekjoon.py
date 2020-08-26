#2007년

import calendar
x,y = map(int,input().split())
day = ['MON','TUE','WED','THU','FRI','SAT','SUN']
a = calendar.weekday(2007,x,y) #weekday(required year, month, day) and return (0~6:Mon~SUN)
print(day[a])