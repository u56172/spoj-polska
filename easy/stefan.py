import sys
input = sys.stdin.readline #bez tego spoj nie zatwierdzał

n = int(input())
suma = 0
max_suma = 0
for i in range(n):
    suma += int(input())
    if suma < 0:
        suma = 0
    elif suma > max_suma:
        max_suma = suma
print(max_suma)