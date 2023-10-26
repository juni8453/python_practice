def solution(nums):
    answer = 0
    count = 0
    memory_num = 0

    # 오름차순 정렬
    nums.sort()

    for num in nums:
        if memory_num < num:
            memory_num = num
            count += 1

    can_eat_count = int(len(nums) / 2)
    if count <= can_eat_count:
        answer = count

    elif count > can_eat_count:
        answer = can_eat_count

    return answer


print(solution([2, 1, 1, 3, 2, 3, 1, 2]))
print(solution([1, 3, 5, 7, 2, 3, 7, 5, 3, 2, 5, 7, 9, 12]))
print(solution([5, 5, 5, 5, 5, 5]))
print(solution([12, 23, 11, 3, 5, 23, 23, 23, 23, 23, 23, 23]))
print(solution([100, 200, 300, 400, 500, 600, 700, 800]))