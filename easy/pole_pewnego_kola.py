import math
r, d = map(float, input().split())
pi = 3.141592654
R = math.sqrt(r**2 - (d/2)**2)
S = round(pi * (R**2), 2)
print(S)
