n = int(input())
spis1 = list(map(int, input().split(' ')[:n]))
spis2 = list(map(int, input().split(' ')[:n]))
spis3 = []
if sorted(spis1) != sorted(spis2):
    print("NO")
else:
    start = 0
    for i in range(len(spis2) - 1):

        if int(spis2[i]) > int(spis2[i + 1]):
            spis3.append([start, i])
            start = i + 1

    if start == len(spis2) - 1:
        spis3.append([start, start])
    else:
        spis3.append([start, len(spis2) - 1])
    result = 0
    for i in spis3:
        if sorted(spis1[i[0]:i[1] + 1]) == sorted(spis2[i[0]:i[1] + 1]):
            result += 1
    if len(spis3) == result:
        print("YES")
    else:
        print("NO")
