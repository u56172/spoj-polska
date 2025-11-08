zestawy = []
wszystkie_czasy = []

ile_test = int(input())
for i in range(ile_test):
    N, M = map(int, input().split())
    zestawy.append((N, M))
    czasy = []
    for j in range(N):
        czasy.append(int(input()))
    wszystkie_czasy.append(czasy)


pudelka_lista = []

for k in range(len(zestawy)):
    N, M = zestawy[k]
    czasy = wszystkie_czasy[k]
    suma = 0
    for czas in czasy:
        suma += 86400 // czas
    if suma % M == 0:
        pudelka = suma // M
    else:
        pudelka = suma // M + 1
    print(pudelka)