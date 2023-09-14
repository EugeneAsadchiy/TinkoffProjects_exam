def find_parent(x, parent):
    x = x - 1
    while x != parent[x]:
        x = parent[x]
    return x


def union(x, y, parent, rank):
    x_parent = find_parent(x, parent)
    y_parent = find_parent(y, parent)

    if x_parent != y_parent:
        if rank[x_parent] < rank[y_parent]:
            parent[x_parent] = y_parent
        elif rank[x_parent] > rank[y_parent]:
            parent[y_parent] = x_parent
        else:
            parent[x_parent] = y_parent
            rank[y_parent] += 1


def main():
    n, m = map(int, input().split())
    parent = list(range(n))
    rank = [0] * n

    for _ in range(m):
        query = input().split()
        if query[0] == '2':
            x, y = map(int, query[1:])
            if find_parent(x, parent) == find_parent(y, parent):
                print("YES")
            else:
                print("NO")
        elif query[0] == '3':
            x = int(query[1])
            print(rank[find_parent(x, parent)])
        else:
            x, y = map(int, query[1:])
            union(x, y, parent, rank)


if __name__ == "__main__":
    main()
