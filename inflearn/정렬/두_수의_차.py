from collections import defaultdict

def solution(nums):
    answer = []
    nums.sort()

    nums_dict = defaultdict(list)
    nums_dict[nums[1] - nums[0]].append([nums[0], nums[1]])

    for i in range(1, len(nums) - 1):
        d_result = nums[i + 1] - nums[i]
        nums_dict[d_result].append([nums[i], nums[i + 1]])

    min_key = 1e9
    for key in nums_dict.keys():
        min_key = min(min_key, key)

    for key, value in nums_dict.items():
        if key == min_key:
            answer.extend(value)

    return answer


print(solution([3, 8, 1, 5, 12]))
print(solution([2, 1, 3, 5, 4]))
print(solution([5, 10, 15, 20, 25, 11]))
print(solution([2, 4, 3, 1, 5, 7, 8, 12, 13, 15, 23]))
print(solution([100, 200, 300, 400, 120, 130, 135, 132, 121]))