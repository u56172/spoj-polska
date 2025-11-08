import sys
zestawy = []
t = int(input())
for j in range(t):
    slowo = str(input())
    zestawy.append(slowo)
for slowo in zestawy:
    for i in range(len(slowo)//2):
        print(slowo[i], end='')
    print('')
#pierwszy
#lubiec
#ktotozrobi