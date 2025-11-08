import sys

zestawy = []

for linia in sys.stdin:
    linia = linia.strip()
    if not linia:
        continue
    A, B, C = map(float, linia.split())
    zestawy.append((A, B, C))

for A, B, C in zestawy:
    delta = B**2 - 4*A*C
    if delta < 0:
        print(0)
    elif delta == 0:
        print(1)
    else:
        print(2)
