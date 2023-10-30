def solution(nums, k):
    window = 0
    total_num = sum(nums)

    # k - 1 크기의 윈도우를 만든다.
    for i in range(len(nums) - k):
        window += nums[i]

    print(f'최초 윈도우 : {window}')

    start = 0
    minN = window
    for end in range(len(nums) - k, len(nums)):
        # 윈도우를 밀면서 가장 작은 윈도우를 찾아낸다
        window += (nums[end] - nums[start])
        minN = min(minN, window)
        start += 1

    return total_num - minN

print(solution([2, 3, 7, 1, 2, 1, 5], 4))
print(solution([1, 2, 3, 5, 6, 7, 1, 3, 9], 5))
print(solution([1, 30, 3, 5, 6, 7], 3))
print(solution([1, 2, 15, 3, 6, 7, 8, 9], 5))
print(solution([12, 5, 6, 12, 34, 35, 13, 3, 7, 8, 9], 7))
