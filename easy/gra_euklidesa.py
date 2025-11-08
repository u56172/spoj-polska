t = int(input())
sumy = []
for i in range(t):
    a, b = map(int, input().split())
    if b > a:
        a, b = b, a
    while a - b > 0 or b - a > 0:
        if b > a:
            a, b = b, a
        a = a - b
    sumy.append(a + b)
for x in sumy:
    print(x)
