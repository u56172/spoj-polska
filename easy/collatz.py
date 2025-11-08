t = int(input())
dane = []

for i in range(t):
    s = int(input())
    dane.append(s)

def ktore(x: int) -> int:
    n = 0
    while x != 1:
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        n += 1
    return n

for i in range(len(dane)):
    print(ktore(dane[i]))
