from collections import defaultdict


def dfs(current_node, graph, visited):
    visited[current_node] = True

    for next_node in graph[current_node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node, graph, visited)


def solution(n, computers):
    answer = 0

    # 먼저 컴퓨터의 연결 정보를 가지고 인접 리스트를 생성한다.
    graph = defaultdict(list)

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                graph[i].append(j)

    # 생각해보면, 연결돼있는 컴퓨터가 있다면(현재 Computer 를 Key 로 한 Value List 가 있다는 뜻)
    # 연결돼있는 컴퓨터가 없을 때 까지 재귀 호출을 하고, 방문 처리가 안된 컴퓨터 즉, 연결돼있지 않았던 컴퓨터를
    # Key 로 해 재귀 호출을 하는 식으로 구성한다.
    # 이렇게 하면, DFS 가 호출되는 횟수 == Network 개수가 되고 이걸 반환하면 끝.

    visited = [False] * n
    for current_node in graph.keys():
        if not visited[current_node]:
            dfs(current_node, graph, visited)
            answer += 1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))