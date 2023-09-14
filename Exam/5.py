def is_possible(graph, x, n):
    visited = [False] * n
    components = 0

    def dfs(v):
        visited[v] = True
        for u, w in graph[v]:
            if not visited[u] and w <= x:
                dfs(u)

    for i in range(n):
        if not visited[i]:
            dfs(i)
            components += 1

    return components == 1

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    edges = []

    for _ in range(m):
        v, u, w = map(int, input().split())
        graph[v - 1].append((u - 1, w))
        graph[u - 1].append((v - 1, w))
        edges.append(w)

    edges.sort()

    left, right = 0, len(edges) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        x = edges[mid]

        if is_possible(graph, x, n):
            result = x
            right = mid - 1
        else:
            left = mid + 1

    print(result)

if __name__ == "__main__":
    main()
