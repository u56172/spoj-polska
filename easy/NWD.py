def nwd(a: int, b: int) -> int:
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a%b
    return a

t = int(input())
for i in range(t):
    a, b = str(input()).split()
    a, b = map(int, (a, b))
    print(nwd(a, b))


