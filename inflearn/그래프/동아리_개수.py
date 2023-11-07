count = 0


def dfs(node, graph, visited):
    visited[node] = True
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node, graph, visited)


def solution(n, edges):
    global count
    count = 0
    graph = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    # 영역 구하기 풀이와 비슷
    for i in range(1, len(graph)):
        if not visited[i]:
            dfs(i, graph, visited)
            count += 1

    return count


print(solution(10, [
    [1, 2], [2, 3], [1, 4], [1, 5], [6, 8], [7, 8], [9, 10]
]))
print(solution(20, [[1, 2], [2, 5], [5, 7], [9, 7], [5, 13], [15, 13], [3, 4],
                    [4, 6], [6, 8], [8, 10],
                    [11, 12], [14, 16], [16, 17], [17, 18], [19, 20]]))
print(solution(7, [
    [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]
]))
print(solution(30, [
    [5, 6], [6, 7]
]))
