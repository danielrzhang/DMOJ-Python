import sys
import itertools
number = list(sys.stdin.readline())
number.remove("\n")
thing = ''.join(number)
perm = list(itertools.permutations(number))
emptyList = []
secondList = []
for i in perm:
    result = ''.join(i)
    if result not in secondList:
        secondList.append(result)
secondList.sort()
itemIndex = secondList.index(thing)
try:
    sys.stdout.write(secondList[itemIndex + 1])
    sys.stdout.flush()
except IndexError:
    sys.stdout.write("0")
    sys.stdout.flush()
