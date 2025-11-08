t = int(input())
wyniki = []

for i in range(t):
    lista = list(map(int, input().split()))
    liczby = lista[1:]
    srednia = sum(liczby) / len(liczby)
    najmniejsza = min(liczby, key=lambda x: abs(x - srednia))
    wyniki.append(najmniejsza)

for wynik in wyniki:
    print(wynik)
