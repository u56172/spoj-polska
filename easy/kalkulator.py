import sys
dane = []
for line in sys.stdin:
    znak, a, b = line.split()
    a = int(a)
    b = int(b)
    dane.append([znak, a, b])

for znak, a, b in dane:
    if znak == '+':
        print(a+b)
    elif znak == '-':
        print(a-b)
    elif znak == '*':
        print(a*b)
    elif znak == '/':
        print(a//b)
    else:
        print(a%b)