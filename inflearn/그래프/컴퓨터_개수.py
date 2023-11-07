count = 0


def dfs(node, graph, visited):
    global count
    count += 1
    visited[node] = True

    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node, graph, visited)


def solution(n, edges):
    global count
    count = 0  # 초기화 안하면 여러 solution 호출 시 count = 0 이 아닌 상태에서 함수가 호출된다.
    graph = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]

    for [a, b] in edges:
        graph[a].append(b)
        graph[b].append(a)

    dfs(1, graph, visited)  # 1번 노드부터 탐색 시작

    return n - count


print(solution(11, [
    [1, 2], [1, 4], [2, 3], [4, 5], [5, 6], [7, 8], [7, 10], [8, 9], [10, 11]
]))
print(solution(12, [
    [1, 2], [1, 7], [1, 8], [1, 6], [8, 11], [11, 12]
]))
print(solution(14, [
    [1, 6], [1, 5], [6, 7], [7, 8], [9, 8], [3, 4], [4, 14]
]))
print(solution(15, [
    [1, 4], [1, 5], [9, 5], [9, 6], [7, 9], [7, 14]
]))
