def find_parent(parent, x):
    # x 의 부모 노드가 있는 상태라면 재귀로 부모노드를 찾는다.
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    # 둘 중 더 작은 값으로 갱신
    if a < b:
        parent[b] = a

    else:
        parent[a] = b


def solution():
    # 6개의 노드 생성
    nodes = [i for i in range(0, 7)]
    union(nodes, 1, 2)
    union(nodes, 2, 3)
    print(nodes)


solution()