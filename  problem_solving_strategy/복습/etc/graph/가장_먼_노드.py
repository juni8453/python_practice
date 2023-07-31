from collections import defaultdict
from collections import deque

def solution(n, vertex):
    answer = 0

    # 양방향 그래프 생성
    graph = defaultdict(list)
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)

    # 인덱스 번호 == 노드 번호
    # 노드별 가중치 기록
    node_dis = [0 for _ in range(n + 1)]

    visited = [False for _ in range(n + 1)]
    visited[1] = True

    queue = deque()
    queue.append((1, 0)) # 최초 시작 노드 1번, 가중치 0

    while queue:
        cur_node, count = queue.popleft()

        for next_node in graph[cur_node]:
            if not visited[next_node]:
                visited[next_node] = True
                node_dis[next_node] = count + 1

                queue.append((next_node, count + 1))

    max_count = max(node_dis)
    for i in range(len(node_dis)):
        if max_count <= node_dis[i]:
            answer += 1

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))

# 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미한다.
# 가장 멀리 떨어진 노드가 몇 개인지 반환