n, m = map(int, input().split())
spis = list(map(int, input().split()))

# Сортируем номиналы купюр в порядке убывания
spis.sort(reverse=True)

stolen_money = []
amount_stolen = 0

for spi in spis:
    l = 0
    while amount_stolen + spi <= n and l != 2:
        l += 1
        amount_stolen += spi
        stolen_money.append(spi)

if amount_stolen == n:
    print(len(stolen_money))
    print(*stolen_money)
else:
    print(-1)

print("gnfjnfdklgm")
