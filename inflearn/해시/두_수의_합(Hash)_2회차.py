from collections import defaultdict


def solution(nums, target):
    answer = []
    nums_dic = defaultdict(bool)

    for num in nums:
        nums_dic[num] = False

    for cur_num in nums:
        if target - cur_num in nums_dic.keys():
            if target - cur_num != cur_num: # 자기 자신 제외
                return sorted([cur_num, target - cur_num])

    return [0, 0]


print(solution([7, 3, 2, 13, 9, 15, 8, 11], 12))
print(solution([21, 12, 30, 15, 6, 2, 9, 19, 14], 24))
