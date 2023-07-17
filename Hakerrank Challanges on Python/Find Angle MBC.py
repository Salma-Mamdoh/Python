import math
AB = int(input())
BC = int(input())
AC = math.sqrt(AB**2 + BC**2)
theta = math.atan2(AB, BC)
theta_degrees = round(math.degrees(theta))
# Print the angle in degrees with a degree symbol
print("{}\u00b0".format(theta_degrees))
