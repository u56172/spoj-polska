import sys

dane = []
for linia in sys.stdin:
    tekst = linia.rstrip('\n')
    dane.append(tekst)

for tekst in dane:
    wynik = []
    for i in tekst:
        if i.isspace():
            wynik.append(' ')
        elif 'A' <= i <= 'Z':
            if i >= 'X':
                wynik.append(chr(ord(i) - 23))
            else:
                wynik.append(chr(ord(i) + 3))
        else:
            wynik.append(i)

    print("".join(wynik))
