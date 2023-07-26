from collections import deque

def solution(progresses, speeds):
    answer = []
    days = deque()

    # 각 작업이 몇 일 더 작업해야하는지 계산 -> days 배열에 저장
    for i in range(len(speeds)):
        a, b = divmod(100 - progresses[i], speeds[i])
        days.append(a if b == 0 else a + 1)

    print(days)

    # days 가 빌 떄 까지 while
    while days:
        # 현재 남은 날짜, 함께 배포할 작업 개수 초기화
        current = days.popleft()
        count = 1

        # current 제외 나머지 탐색
        # 같이 배포해야하는 경우 count 추가, 알아서 비교하게 큐의 가장 앞 날려버림
        while days and current >= days[0]:
            count += 1
            days.popleft()

        # 같이 배포하는 경우가 아니라면,
        answer.append(count)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))