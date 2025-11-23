t = int(input())
dane = []
for _ in range(t):
    dane.append(input().split())

for dana in dane:
    n = int(dana[0])
    x = int(dana[1])
    y = int(dana[2])

    for i in range(1, n):
        if i % x == 0 and i % y != 0:
            print(i, end=' ')
    print()