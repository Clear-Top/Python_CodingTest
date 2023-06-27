import sys
input = sys.stdin.readline

month, day = map(int, input().split())

DAY_OF_MONTH = {
    '1':31,
    '2':28,
    '3':31,
    '4':30,
    '5':31,
    '6':30,
    '7':31,
    '8':31,
    '9':30,
    '10':31,
    '11':30,
    '12':31,
}

WEEK=['SUN','MON','TUE','WED','THU','FRI','SAT']

sum = 0
for m in range(1,month):
    sum+=DAY_OF_MONTH[str(m)]
print
print(WEEK[(sum+day)%7])
    