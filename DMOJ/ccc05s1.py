import sys
number = int(sys.stdin.readline())
for i in range(number):
    phoneNumber = list(sys.stdin.readline())
    for i in phoneNumber:
        if i == "-":
            phoneNumber.remove("-")
    for i in phoneNumber:
        if (i == "A") or (i == "B") or (i == "C"):
            index = phoneNumber.index(i)
            phoneNumber.remove(i)
            phoneNumber.insert(index, "2")

        if (i == "D") or (i == "E") or (i == "F"):
            index = phoneNumber.index(i)
            phoneNumber.remove(i)
            phoneNumber.insert(index, "3")

        if (i == "G") or (i == "H") or (i == "I"):
            index = phoneNumber.index(i)
            phoneNumber.remove(i)
            phoneNumber.insert(index, "4")

        if (i == "J") or (i == "K") or (i == "L"):
            index = phoneNumber.index(i)
            phoneNumber.remove(i)
            phoneNumber.insert(index, "5")

        if (i == "M") or (i == "N") or (i == "O"):
            index = phoneNumber.index(i)
            phoneNumber.remove(i)
            phoneNumber.insert(index, "6")

        if (i == "P") or (i == "Q") or (i == "R") or (i == "S"):
            index = phoneNumber.index(i)
            phoneNumber.remove(i)
            phoneNumber.insert(index, "7")

        if (i == "T") or (i == "U") or (i == "V"):
            index = phoneNumber.index(i)
            phoneNumber.remove(i)
            phoneNumber.insert(index, "8")

        if (i == "W") or (i == "X") or (i == "Y") or (i == "Z"):
            index = phoneNumber.index(i)
            phoneNumber.remove(i)
            phoneNumber.insert(index, "9")

    phoneNumber.pop()
    while len(phoneNumber) > 10:
        phoneNumber.pop()

    for i in range(3, 11, 4):
        phoneNumber.insert(i, "-")
    result = ''.join(phoneNumber)
    sys.stdout.write(result + "\n")
