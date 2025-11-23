import math
n = int(input())
liczby = []
for i in range(n):
    liczby.append(int(input()))

for liczba in liczby:
    if liczba == 1:
        print('NIE')
    elif liczba == 2:
        print('TAK')
    else:
        dzielniki = []
        for i in range(2, int(math.sqrt(liczba)) + 1):
            if liczba % i == 0:
                dzielniki.append(i)
        if len(dzielniki) == 0:
            print('TAK')
        else:
            print('NIE')