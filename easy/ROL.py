t = int(input())

lista = []
for i in range(t):
    dane = list(map(int, input().split()))
    n = dane[0]
    liczby = dane[1:]
    liczby = liczby[1:] + liczby[:1]
    lista.append(liczby)

for i in lista:
    print(*i)
