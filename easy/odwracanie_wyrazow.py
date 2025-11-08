import sys

wyrazy = []
for linia in sys.stdin:
    linia = str(linia).strip()
    wyrazy.append(linia)

for wyraz in wyrazy:
    print(wyraz[::-1])