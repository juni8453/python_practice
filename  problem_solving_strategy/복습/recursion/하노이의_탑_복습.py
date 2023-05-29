def hanoi(n, start, to, mid, answer): # 시작, 도착, 경유
    if n == 1:
        return answer.append([start, to])

    # 가장 큰 원반을 제외한 나머지 n - 1 개의 원반을 도착 기둥 (여기서는 경유지) 를 거쳐 경유 기둥 (여기서는 도착지) 로 이동
    hanoi(n - 1, start, mid, to, answer)

    # n - 1 개의 원반 이동이 끝났다면 마지막 하나 남아있는 원반을 직접 도착지로 이동
    answer.append([start, to])

    # 앞선 재귀의 결과로 경유지에 있는 n - 1 개의 원반을 시작 기둥을 거쳐 도착지로 이동
    hanoi(n - 1, mid, to, start, answer)

# 하노이의 탑의 중요 전제 조건은, 가장 큰 원반을 제외한 나머지 n - 1 개의 원반을
# 먼저 경유 기둥으로 옮기고, 가장 큰 원반을 목적 기둥에 옮길 수 있다는 것.
def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)

    return answer


print(solution(2))