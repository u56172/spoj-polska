t = int(input())
dane = []
for i in range(t):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    s = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    dane.append(s)
for i in dane:
    print('TAK') if i == 0 else print('NIE')