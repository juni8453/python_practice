def solution(n, times):
    answer = 1e15

    # times 리스트에서 최소 시간을 찾는 문제가 아니기 때문에 times 리스트를 정렬할 필요는 없다.
    # 왼쪽은 리스트의 최소값, 오른쪽은 가장 최악의 상황의 시간으로 설정
    left = min(times)
    right = max(times) * n

    while left <= right:
        mid = (left + right) // 2
        checked_people_count = 0

        # 현재 임의의 mid 시간을 기준으로 총 몇 명을 검사할 수 있는지 확인한다.
        for time in times:
            checked_people_count += mid // time

        # 임의의 mid 시간을 기준으로 주어진 n 명 보다 더 많이 검사가 가능하다면, mid 시간이 넉넉하다는 뜻.
        # 즉, mid 시간을 줄여야한다.
        # if checked_people_count >= n:
        #     answer = min(answer, mid)
        #     right = mid - 1
        if checked_people_count > n:
            right = mid - 1

        # 임의의 mid 시간을 기준으로 주어진 n 명 보다 적게 검사가 가능하다면, mid 시간이 부족하다는 뜻.
        # 즉, mid 시간을 늘려야한다.
        elif checked_people_count < n:
            left = mid + 1

        else:
            answer = min(answer, mid)

    return answer


print(solution(6, [7, 10]))
