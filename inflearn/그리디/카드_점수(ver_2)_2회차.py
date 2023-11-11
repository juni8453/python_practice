def solution(nums, k):
    answer = 0
    window = 0
    n_len = len(nums)
    window_len = n_len - k
    n_sum = sum(nums)

    # 최초 윈도우를 설정
    # 전체 길이 - k -> 윈도우 크기
    for i in range(window_len):
        window += nums[i]


    # n_sum - window 의 결과로 가장 큰 값이 정답
    start = 0
    window_min = window
    for end in range(len(nums) - k, len(nums)):
        window = window + nums[end] - nums[start]
        window_min = min(window_min, window)
        start += 1

    # print(f'window_min = {window_min}')
    answer = n_sum - window_min

    return answer


print(solution([2, 3, 7, 1, 2, 1, 5], 4))
print(solution([1, 2, 3, 5, 6, 7, 1, 3, 9], 5))
print(solution([1, 30, 3, 5, 6, 7], 3))
print(solution([1, 2, 15, 3, 6, 7, 8, 9], 5))
print(solution([12, 5, 6, 12, 34, 35, 13, 3, 7, 8, 9], 7))