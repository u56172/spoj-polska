N = int(input())
dane = []
for i in range(N):
    dane.append(input())

liczba_znakow = {}

for s in dane:
    for litera in s:
        if litera not in liczba_znakow:
            liczba_znakow[litera] = 1
        else:
            liczba_znakow[litera] += 1

for ch in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if ch in liczba_znakow:
        print(ch, liczba_znakow[ch])
