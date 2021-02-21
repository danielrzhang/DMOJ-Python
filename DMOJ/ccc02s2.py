import sys
num1 = int(sys.stdin.readline())
num2 = int(sys.stdin.readline())

if (num1 > num2) and (num1 % num2 == 0):
    result = int(num1 / num2)
    sys.stdout.write(str(result))

elif (num1 / num2 == 0):
    answer = 0
    sys.stdout.write(str(answer))
else:
    if num1 > num2:
        for i in range(1, num2 + 1):
            if (num1 % i == 0) and (num2 % i == 0):
                newNum1 = num1 / i
                newNum2 = num2 / i
        wholeNumber = int(newNum1 / newNum2)
        resultNum1 = int(newNum1 - (wholeNumber * newNum2))
        resultNum2 = int(newNum2)
        sys.stdout.write(str(wholeNumber) + " " + str(resultNum1) + "/" + str(resultNum2))
    else:
        for i in range(1, num1 + 1):
            if (num1 % i == 0) and (num2 % i == 0):
                newNum1 = str(int(num1 / i))
                newNum2 = str(int(num2 / i))
        sys.stdout.write(newNum1 + "/" + newNum2)
sys.stdout.flush()
