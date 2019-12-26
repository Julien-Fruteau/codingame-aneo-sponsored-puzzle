import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

speed = int(input())
light_count = int(input())
print("{} {}".format(speed, light_count), file=sys.stderr)
for i in range(light_count):
    distance, duration = [int(j) for j in input().split()]
    print("{} {}".format(distance, duration), file=sys.stderr)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(50)