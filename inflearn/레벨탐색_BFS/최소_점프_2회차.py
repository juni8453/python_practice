from collections import deque


def solution(home):
    visited = [False for _ in range(10001)]
    queue = deque()
    queue.append((0, 0))
    visited[0] = True

    while queue:
        for i in range(len(queue)):
            cur_point, cur_count = queue.popleft()

            if cur_point == home:
                return cur_count

            for distance in [cur_point + 1, cur_point - 1, cur_point + 5]:
                if 0 <= distance <= 10000 and not visited[distance]:
                    visited[distance] = True
                    queue.append((distance, cur_count + 1))

print(solution(10))
print(solution(14))
print(solution(25))
print(solution((24)))
print(solution((345)))