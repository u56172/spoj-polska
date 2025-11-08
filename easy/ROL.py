n = int(input())
lista = []

for i in range(n):
    dane = input().split()
    liczby = list(map(int, dane[2:]))
    lista.append(liczby)

print(lista)
