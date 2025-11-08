t = int(input())
wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
dane = []
for i in range(t):
    pesel = input().strip()
    dane.append(pesel)

for pesel in dane:
    suma = 0
    for i in range(11):
        suma += int(pesel[i]) * wagi[i]
    print('D' if suma % 10 == 0 else 'N')
