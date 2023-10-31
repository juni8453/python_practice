# lower bound search : 찾고자 하는 값보다 크거나 같은 값 중 가장 작은 값을 찾는다.

def solution(nums, target):
    start = 0
    end = len(nums)

    while start < end: # start 와 mid 가 곂치는 경우 탈출 (일반 이진탐색과 다름)
        mid = (start + end) // 2

        if target > nums[mid]:
            start = mid + 1
        else:
            end = mid

    if end == len(nums): # 못 찾은 경우
        return -1

    else:
        return end


print(solution([100, 120, 150, 160, 165, 170, 172, 180, 190, 200], 172))


