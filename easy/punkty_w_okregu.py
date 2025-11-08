import math
xo, yo, r = map(int, input().split())
n = int(input())
punkty = []
for i in range(n):
    xi, yi = map(int, input().split())
    punkty.append([xi, yi])

for j in punkty:
    xi = j[0]
    yi = j[1]
    odl = math.sqrt((xi-xo)**2+(yi-yo)**2)
    print('I' if odl < r else 'E' if odl == r else 'O')