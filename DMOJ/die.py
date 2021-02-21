top = str(input())
middle = str(input())
bottom = str(input())
if (top == ":::") and (middle == ":o:") and (bottom == ":::"):
    print(1)
elif ((top == "o::") and (middle == ":::") and (bottom == "::o")) or ((top == "::o") and (middle == ":::") and (bottom == "o::")):
    print(2)
elif ((top == "o::") and (middle == ":o:") and (bottom == "::o")) or ((top == "::o") and (middle == ":o:") and (bottom == "o::")):
    print(3)
elif (top == "o:o") and (middle == ":::") and (bottom == "o:o"):
    print(4)
elif (top == "o:o") and (middle == ":o:") and (bottom == "o:o"):
    print(5)
elif ((top == "ooo") and (middle == ":::") and (bottom == "ooo")) or ((top == "o:o") and (middle == "o:o") and (bottom == "o:o")):
    print(6)
else:
    print("unknown")
