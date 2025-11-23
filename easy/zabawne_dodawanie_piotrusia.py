t = int(input())
dane = []
for i in range(t):
    dane.append(int(input()))

for n in dane:
    liczba_teraz = 0

    while True:
        s = str(n)
        if s == s[::-1]:
            break
        odwrocona = int(s[::-1])
        n = n + odwrocona
        liczba_teraz += 1

    print(n, liczba_teraz)