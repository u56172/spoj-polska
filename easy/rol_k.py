n, k = map(int, input().split())
lista = list(map(int, input().split()))
nowa = lista[k:] + lista[:k]
print(*nowa)