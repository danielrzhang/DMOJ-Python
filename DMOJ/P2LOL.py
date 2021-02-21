import sys
number = int(sys.stdin.readline())
xList = []
yList = []
for i in range(number):
    x, y = map(int, sys.stdin.readline().split())
    xList.append(x)
    yList.append(y)

smallX = min(xList)
largeX = max(xList)

smallY = min(yList)
largeY = max(yList)

length = largeX - smallX
width = largeY - smallY

sys.stdout.write(str(length * width))
