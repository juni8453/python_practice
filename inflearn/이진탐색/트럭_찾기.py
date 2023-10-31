# 트럭이 실을 수 있는 제한 무게와 현수의 총 짐 무게가 같을 수 있으니 lower bound search(bisect_left) 사용

from bisect import bisect_left

def solution(nums, target):
    start = 0
    end = len(nums)

    while start < end: # 일반 이진탐색과 다르게 start == end 인 경우 멈추도록
        mid = (start + end) // 2
        if target > nums[mid]:
            start = mid + 1

        else:
            end = mid

    if end == len(nums):
        return -1

    else:
        return end

# bisect_left 로 풀이
def solution(nums, target):
    answer = bisect_left(nums, target)

    if answer == len(nums):
        return -1
    else:
        return answer


print(solution([100, 120, 150, 160, 165, 170, 175, 180, 190, 200], 170))
print(solution([200, 250, 260, 265, 275, 290, 300, 325, 350, 370], 270))
print(solution([50, 55, 60, 65, 70, 80, 90], 80))
print(solution([20, 30, 40, 50, 60, 70], 90))
print(solution([10, 30, 50, 70, 80, 90, 100, 110, 120], 115))