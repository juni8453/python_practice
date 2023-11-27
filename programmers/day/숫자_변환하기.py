from collections import deque


def solution(x, y, n):
    queue = deque()
    queue.append((x, 0))
    visited = [False for _ in range(1000001)]
    visited[x] = True

    while queue:
        cur_x, cur_count = queue.popleft()

        if cur_x == y:
            return cur_count

        for next_x in [cur_x + n, cur_x * 2, cur_x * 3]:
            if 1 <= next_x <= 1000000 and not visited[next_x]:
                visited[next_x] = True
                queue.append((next_x, cur_count + 1))

    # 찾을 수 없다면 -1 반환
    return -1

# x + n
# x * 2
# x * 3
# x == y 이 되기 위한 최소 연산 횟수를 return
# x 가 y 로 바뀔 수 없다면 -1 을 return