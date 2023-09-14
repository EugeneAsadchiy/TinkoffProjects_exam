n, s = map(int, input().split())
spis = list(map(int, input().split(' ')[:n]))
max = 0
for i in spis:
    if i > max and i <= s:
        max = i
print(max)
