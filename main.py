import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

max_speed = int(input())
# max_speed = 90  # km/h
light_count = int(input())
print("max_speed, light_count = {} {}".format(
    max_speed, light_count), file=sys.stderr)
tmp_speeds = [speed for speed in range(1, max_speed + 1)]

for i in range(light_count):
    distance, duration = [int(j) for j in input().split()]
    print("Feu {} : distance, duration = {} {}".format(
          i, distance, duration), file=sys.stderr)

    for speed in list(tmp_speeds):
        # print(speed)
        speedSec = (speed * 1000) / 3600
        timeToLight = distance / speedSec
        # print("speed, timeToLight = {}, {}".format(speed, timeToLight),
        #       file=sys.stderr)
        if math.floor(timeToLight / duration) % 2 == 1:
            # print("remove speed = {}".format(speed), file=sys.stderr)
            tmp_speeds.pop(tmp_speeds.index(speed))

print("tmp_speeds = {}".format(tmp_speeds), file=sys.stderr)
# print("solution = {}".format(max(tmp_speeds)), file=sys.stderr)

print(max(tmp_speeds))
