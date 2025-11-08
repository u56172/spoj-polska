import sys
dane = []
for i in sys.stdin:
    dane.append(int(i))
suma = 0
for i in dane:
    suma = suma + i
    print(suma)

