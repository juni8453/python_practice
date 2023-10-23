from collections import defaultdict

def solution(nums, target):
    answer = [0, 0]
    nums_dic = defaultdict(int)

    for num in nums:
        nums_dic[num] += 1

    # 찾고 싶은 key = target - 기준 key
    # 자기 자신 제외
    for key in nums_dic.keys():
        want_key = target - key
        if want_key != key and want_key in nums_dic.keys():
            return sorted([key, want_key])

    return answer


print(solution([7, 3, 2, 13, 9, 15, 8, 11], 12))
print(solution([21, 12, 30, 15, 6, 2, 9, 19, 14], 24))
print(solution([12, 18, 5, 8, 21, 27, 22, 25, 16, 2], 28))
print(solution([7, 5, 12, -9, -12, 22, -30, -35, -21], -14))
print(solution([7, 5, 12, 20], 15))