# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB = int(input())
BC = int(input())
AC = math.sqrt(AB**2+BC**2)
theta = math.acos(BC/AC )
print(str(round(math.degrees(theta))),'\u00B0',sep='')