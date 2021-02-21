import sys
hour, minute = map(int, sys.stdin.readline().split())
extraMinutes = int(sys.stdin.readline())

newMinutes = str((minute + extraMinutes) % 60)
newHour = int(int(minute + extraMinutes) / 60)

resultHour = str((hour + newHour) % 24)

sys.stdout.write(resultHour + " " + newMinutes)
sys.stdout.flush()
