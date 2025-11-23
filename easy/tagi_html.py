import sys

dane = []
for linia in sys.stdin:
    dane.append(linia)

for linia in dane:
    wynik = ""
    i = 0

    while i < len(linia):
        if linia[i] == '<':
            wynik += '<'
            i += 1
            while True:
                if i >= len(linia):
                    break
                if linia[i] == '>':
                    wynik += '>'
                    i += 1
                    break
                wynik += linia[i].upper()
                i += 1
        else:
            wynik += linia[i]
            i += 1

    print(wynik, end='')