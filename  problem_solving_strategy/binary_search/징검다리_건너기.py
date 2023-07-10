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

        for stone in stones:
            if stone < mid:
                skip_stone += 1

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