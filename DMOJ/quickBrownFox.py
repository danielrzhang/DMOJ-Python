number = int(input())
letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for m in range(number):
    emptyList = []
    string = str(input())
    newString = string.lower()
    newStringList = newString

    for i in letterList:
        if i not in newStringList:
            emptyList.append(i)
    combined = ''.join(emptyList)
    if emptyList == []:
        print("pangram")
    else:
        print("missing " + combined)
