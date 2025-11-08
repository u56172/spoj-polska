t = int(input())
for i in range(t):
    dane = list(map(int, input().split()))
    liczby = dane[1:]
    print(*liczby[::-1])
