hour = int(input())

if hour == 0:
    print(12)
if hour in range(1, 12):
    print(str(hour))
if hour in range(13, 23):
    print((hour - 1) % 12 + 1)
#I Made Changes