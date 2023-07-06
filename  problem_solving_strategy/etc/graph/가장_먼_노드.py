from collections import defaultdict
from collections import deque


def solution(n, vertex):
    answer = 0
    graph = defaultdict(list)

    # 문제 제시사항에 따라 양방향 그래프 생성
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)

    # Root 노드 ~ 각 노드의 거리를 저장하는 리스트, 방문 체크 리스트 추가
    node_distance = [0 for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]

    # BFS 사용을 위해 queue, visited 초기화
    queue = deque()
    queue.append((1, 0))
    visited[1] = True

    while queue:
        cur_node, count = queue.popleft()
        node_distance[cur_node] = count

        for next_node in graph[cur_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, count + 1))

    for distance in node_distance:
        if max(node_distance) == distance:
            answer += 1

    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))