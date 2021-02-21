import sys

n = int(sys.stdin.readline().strip())
counter = 1

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    counter = counter * ((b - a) / b)

sys.stdout.write("%.6f" % counter)
sys.stdout.flush()
