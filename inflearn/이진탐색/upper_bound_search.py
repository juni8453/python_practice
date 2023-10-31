# upper bound search : 찾고자 하는 값보다 큰 값 중 가장 작은 값을 찾는다.
def solution(nums, target):
    start = 0
    end = len(nums)

    while start < end:
        mid = (start + end) // 2

        if target >= nums[mid]:
            start = mid + 1

        else:
            end = mid

    if end == len(nums):
        return -1

    else:
        return end


print(solution([100, 120, 150, 160, 165, 170, 172, 180, 190, 200], 172))