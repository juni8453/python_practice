def solution(nums, target):
    answer = -1
    start = 0
    end = len(nums)

    while start <= end: # 곂쳤을 떄 판단 필요
        mid = (start + end) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            end = mid - 1

        if nums[mid] < target:
            start = mid + 1

    return answer


print(solution([2, 5, 7, 8, 10, 15, 20, 24, 25, 30], 8))
print(solution([-3, 0, 2, 5, 8, 9, 12, 15], 0))
print(solution([-5, -2, -1, 3, 8, 9, 12, 17, 23], 2))
print(solution([3, 6, 9, 12, 17, 29, 33], 3))
print(solution([1, 2, 3, 4, 5, 7, 9, 11, 12, 15, 16, 17, 18], 18))