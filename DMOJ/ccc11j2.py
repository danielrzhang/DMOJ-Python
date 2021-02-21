import sys
humidity = int(sys.stdin.readline())
maxTime = int(sys.stdin.readline())

for i in range(maxTime):
    altitude = (-6 * (i ** 4)) + (humidity * (i ** 3)) + (2 * (i ** 2)) + i
    if (altitude <= 0) and (i != 0):
        result = True
        maxTime = i
        break

    else:
        result = False

if result:
    sys.stdout.write("The balloon first touches ground at hour: \n")
    sys.stdout.write(str(maxTime))

else:
    sys.stdout.write("The balloon does not touch ground in the given time.")
