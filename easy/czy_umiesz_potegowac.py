D = int(input())
dane = []
for i in range(D):
    a, b = map(int, input().split())
    dane.append([a, b])
for i in dane:
    a = i[0]
    b = i[1]
    wynik = pow(a, b, 10)
    print(wynik)