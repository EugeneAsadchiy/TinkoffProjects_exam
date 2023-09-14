# Функция для инициализации DSU
def make_set(n):
    parent = list(range(n))
    size = [1] * n
    return parent, size

# Функция для поиска корня множества
def find_set(x, parent):
    if parent[x] == x:
        return x
    parent[x] = find_set(parent[x], parent)
    return parent[x]

# Функция для объединения двух множеств
def union_sets(x, y, parent, size):
    x = find_set(x, parent)
    y = find_set(y, parent)
    if x != y:
        if size[x] < size[y]:
            x, y = y, x
        parent[y] = x
        size[x] += size[y]

n, m = map(int, input().split())
parent, size = make_set(n)

answers = []

for _ in range(m):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x, y = query[1] - 1, query[2] - 1
        union_sets(x, y, parent, size)
    elif query[0] == 2:
        x, y = query[1] - 1, query[2] - 1
        if find_set(x, parent) == find_set(y, parent):
            answers.append("YES")
        else:
            answers.append("NO")
    elif query[0] == 3:
        x = query[1] - 1
        root = find_set(x, parent)
        count = 0
        for i in range(n):
            if find_set(i, parent) == root:
                count += 1
        answers.append(str(count))

for ans in answers:
    print(ans)

