import sys

dane = []
for line in sys.stdin:
    line = line.strip()
    if line == "0":
        break
    dane.append(int(line))

for i in dane:
    print("TAK" if i % 15 == 0 else "NIE")
