import sys

for linia in sys.stdin:
    dane = linia.strip()
    a, b, c = map(float, dane.split())
    if a + b > c and a + c > b and b + c > a:
        print(1)
    else:
        print(0)
