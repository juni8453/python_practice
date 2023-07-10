def solution(stones, k):
    # 총 몇 명이 다리를 건널 수 있는가 ?
    # len(stones) <= 200,000 stone[i] <= 200,000,000
    # 즉, 모든 디딤돌이 2억이라면 2억명까지 계산이 들어가므로 시간 초과 (완전탐색으로 풀이 불가)
    # 임의의 mid 값을 다리를 건널 수 있는 인원 수라고 하고 start = 0, end = max(stones) 로 초기화
    answer = -1e15
    start, end = 0, max(stones)

    while start <= end:
        skip_stone = 0
        mid = (start + end) // 2

        # 현재 디딤발 허용 횟수와 임의의 통과 인원수를 뺀 값이 0 보다 작거나 같다면 (즉, mid 명이 지나갔을 떄 음수 또는 0이 되는 경우)
        # 건너뛰어야 하므로 skip_stone 을 하나 추가한다.
        for stone in stones:
            if stone < mid:
                skip_stone += 1

                # 건너뛰어야 하는 디딤돌 개수가 한 번에 건너뛸 수 있는 디딤돌 개수인 k 보다 같거나 많으면 (같아도 건너뛰지 못하니까)
                # 더 이상 탐색의 의미가 없으므로 범위를 줄이고 for 문을 탈출한다.
                if skip_stone >= k:
                    break

            elif stone >= mid:
                skip_stone = 0

        if skip_stone >= k:
            end = mid - 1

        elif skip_stone < k:
            answer = max(answer, mid)
            start = mid + 1

    return answer

print(solution([2,4,5,3,2,1,4,2,5,1], 3))