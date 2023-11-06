from collections import deque


def solution(home):
    queue = deque()
    check = [False for _ in range(10001)]
    queue.append((0, 0)) # 최초 위치 0 (놀이터) / 현재까지 점프수(Level)
    check[0] = True # 최초 위치 체크

    while queue:
        for i in range(len(queue)): # 큐에 담긴 현재 레벨의 모든 노드를 탐색
            cur_point, cur_count = queue.popleft()

            if cur_point == home:
                return cur_count

            for dis in [cur_point - 1, cur_point + 1, cur_point + 5]:
                if 0 <= dis <= 10000 and not check[dis]: # 좌표 값을 넘어가지 않으면서, 아직 탐색하지 않은 곳이라면
                    queue.append((dis, cur_count + 1))
                    check[dis] = True

    return 0


print(solution(10))
print(solution(14))
print(solution(25))
print(solution(24))
print(solution(345))
