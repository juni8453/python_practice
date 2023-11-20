def solution(nums, weight):
    nums.sort()

    # lower bound search 구현
    # 찾고자하는 값보다 같거나 큰 값 중 가장 작은 값
    start = 0
    end = len(nums)

    while start < end:
        mid = (start + end) // 2

        if weight > nums[mid]:
            start = end + 1

        else:
            end = mid

    if end == len(nums):
        return -1

    else:
        return end


print(solution([100, 120, 150, 160, 165, 170, 175, 180, 190, 200], 170))