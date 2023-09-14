a, b, c, d = map(int, input().split())
if b > d:
    result = a
else:
    result = a + (d - b) * c
print(result)
