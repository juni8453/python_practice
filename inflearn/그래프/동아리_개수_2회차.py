def dfs(cur_node, graph, checked):
    checked[cur_node] = True

    # 모든 학생이 동아리를 다니는데, 연결된 다른 학생(next_node) 가 없다면 자기 혼자 그 동아리 다닌다는 뜻
    # 그대로 빠져나가서 answer 1 증가
    for next_node in graph[cur_node]:
        if not checked[next_node]:
            dfs(next_node, graph, checked)


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    checked = [False for _ in range(n + 1)]

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, len(graph)):
        if not checked[i]:
            # 탐색 시작
            dfs(i, graph, checked)
            answer += 1

    return answer


print(solution(10, [
    [1, 2], [2, 3], [1, 4], [1, 5], [6, 8], [7, 8], [9, 10]
]))

print(solution(30, [
    [5, 6], [6, 7]
]))
