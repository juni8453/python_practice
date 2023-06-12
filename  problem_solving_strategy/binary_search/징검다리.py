def solution(distance, rocks, n):
    answer = 0

    # 시작, 끝 범위를 정하고 rocks 를 오름차순 정렬한다.
    start, end = 0, distance
    # [2, 11, 14, 17, 21]
    rocks.sort()

    while start <= end:
        mid = (start + end) // 2
        del_stone = 0 # 제거한 바위 수
        pre_stone = 0 # 이전 바위 위치

        for rock in rocks:
            # 현재 바위 위치와 이전 바위 위치를 뺀 값이 임의의 최소 거리 값보다 작다면 바위를 제거한다.
            if rock - pre_stone < mid:
                del_stone += 1

            else:
                pre_stone = rock

        if del_stone > n:
            end = mid - 1

        else:
            answer = mid
            start = mid + 1

    return answer

# 최종 길이, 각 바위 위치, 제거할 바위 개수
print(solution(25, [2, 14, 11, 21, 17], 2))