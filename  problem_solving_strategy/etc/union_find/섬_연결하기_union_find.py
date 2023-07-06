def find(parents, x):
    # 연결된 노드가 있다면, 그 부모를 찾아 return
    if x != parents[x]:
        return find(parents, parents[x])

    return x


def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)

    # 더 작은 값으로 부모 노드 갱신
    if a < b:
        parents[b] = a

    else:
        parents[a] = b


def solution(n, costs):
    answer = 0

    # 최소 간선 비용으로 모든 섬이 통행할 수 있도록 다리를 연결
    # 1. 간선 비용 오름차순 정렬
    costs = sorted(costs, key=lambda x: x[2])

    # 2. Union_Find 위한 셋팅
    parents = [i for i in range(n)]

    # 3. Union-Find 실행
    for i in range(len(costs)):
        # 각 노드가 연결되어있지 않은 상태라면 연결 후 간선 비용 추가
        if find(parents, costs[i][0]) != find(parents, costs[i][1]):
            union(parents, costs[i][0], costs[i][1])
            answer += costs[i][2]

    return answer


print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))