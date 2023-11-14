def solution(nums):
    answer = -1
    start = 0
    end = len(nums) - 1

    while start <= end:
        index = (start + end) // 2

        if nums[index] == index:
            return index

        # 만약 nums 의 원소 값이 현재 기준 index 보다 크다면, 기준 인덱스 오른쪽 값들은 모두 어긋난 경우이므로
        # end 를 기준 값 - 1 로 초기화한다.
        elif nums[index] > index:
            end = index - 1

        elif nums[index] < index:
            start = index + 1

    return answer

print(solution([-3, -2, 0, 1, 3, 5, 8, 9, 12]))
print(solution([-10, -5, -2, 0, 4, 6, 7, 8]))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(solution([-5, -3, 0, 1, 2, 3, 4, 7]))
print(solution([0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))