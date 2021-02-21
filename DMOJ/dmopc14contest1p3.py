number = int(input())
emptyList = []
arb1 = 0
arb2 = 0
counter = 0
for i in range(number):
    i = int(input())
    emptyList.append(i)
number2 = int(input())
for j in range(number2):
    j = int(input())
    emptyList.append(j)
while counter != (number + number2):
    divisor = number + 1
    for k in emptyList[:number]:
        arb1 += k
    for l in emptyList[number:]:
        arb2 += l
        result = (arb1 + arb2) / divisor
        print(round(result, 3))
        if counter == number2:
            break
        counter += 1
        divisor += 1
    break
