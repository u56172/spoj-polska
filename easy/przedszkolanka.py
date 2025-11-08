N = int(input())
dane = []
for i in range(N):
    a, b = map(int, input().split())
    dane.append([a, b])

def nwd(a: int, b: int) -> int:
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

def nww(a: int, b: int) -> int:
    return a*b//nwd(a, b)

wynik = []
for a, b in dane:
    wynik.append(nww(a, b))

for w in wynik:
    print(w)