C = int(input())
wyrazy = []
for i in range(C):
    wyrazy.append(input().strip())

for slowo in wyrazy:
    i = 0
    while i < len(slowo):
        k = slowo[i]
        licznik = 1

        j = i + 1
        while j < len(slowo) and slowo[j] == k:
            licznik += 1
            j += 1

        if licznik > 2:
            print(k, licznik, sep='', end='')
        elif licznik == 2:
            print(k * 2, end='')
        else:
            print(k, end='')
        i = j
    print()
