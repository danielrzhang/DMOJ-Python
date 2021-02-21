import sys

longString = list(sys.stdin.readline())
numInput = int(sys.stdin.readline())

sortList = []
longString.pop()

for i in range(len(longString)):
    length = longString[i:i+numInput]
    if len(length) < numInput:
        break
    else:
        result = ''.join(length)
        sortList.append(result)

sortList.sort()
sys.stdout.write(sortList[0])
