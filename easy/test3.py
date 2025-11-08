import sys

tablica = []
poprzedni = None

for line in sys.stdin:
    i = int(line.strip())
    print(i)

    if i == 42 and poprzedni is not None and poprzedni != 42:
        tablica.append(i)
        if len(tablica) == 3:
            break

    poprzedni = i
