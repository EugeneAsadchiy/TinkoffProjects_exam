s = input()
spis = []
result = 0
for i in s:
    spis.append(i)
d = {
    "s": 0,
    "h": 0,
    "e": 0,
    "r": 0,
    "i": 0,
    "f": 0,
}
for i in spis:
    for key, value in d.items():
        if str(i) == key:
            d[key] = value + 1
result = min(d.values())
if result * 2 <= d["f"]:
    print(result)
else:
    print(0)
