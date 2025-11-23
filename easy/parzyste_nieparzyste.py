t = int(input())
dane = []
for i in range(t):
    dane.append(input().split())

for dana in dane:
    n = int(dana[0])
    for i in range(2, n + 1, 2):
        print(dana[i], end=' ')
    for i in range(1, n + 1, 2):
        print(dana[i], end=' ')
    print()