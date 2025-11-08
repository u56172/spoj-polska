a, b, c = map(float, input().split())
if a == 0 and b == c:
    print('NWR')
elif a == 0:
    print('BR')
else:
    x = (c - b) / a
    print(f"{x:.2f}")