from math import sqrt
numTriangle = int(input())
for points in range(numTriangle):
  x1, y1, x2, y2, x3, y3 = map(int, input().split())

  # Perimeter
  side1 = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
  side2 = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
  side3 = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
  perimeter = side1 + side2 + side3

  # Area
  semiPerimeter = (side1 + side2 + side3) / 2
  area = sqrt(semiPerimeter * (semiPerimeter - side1) * (semiPerimeter - side2) * (semiPerimeter - side3))
  print("%.2f" % area, "%.2f" % perimeter)
