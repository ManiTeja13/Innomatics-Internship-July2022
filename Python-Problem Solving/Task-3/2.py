
import math
a = int(input())
b = int(input())
M = math.sqrt(a**2+b**2)
theta = math.acos(b/M )
print(int(round(math.degrees(theta),0)),'\u00B0',sep='')