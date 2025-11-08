m, n = map(int, input().split())
lista = []
for _ in range(m):
    lista.append(list(map(int, input().split())))
transpoza = map(list, zip(*lista))
for i in transpoza:
    print(*i)
