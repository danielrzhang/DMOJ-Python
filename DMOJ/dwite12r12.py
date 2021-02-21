import sys
from math import floor

for i in range(5):
    firstNum, secondNum = map(int, sys.stdin.readline().split())

    sumOfNums = firstNum + secondNum
    decimalForm = firstNum / sumOfNums
    result = decimalForm * 10
    wholeNumber = floor(result)
    print(wholeNumber * "*" + (10 - wholeNumber) * ".")
