def solution(nums):
    answer = 0
    stack = []

    # 샌드위치를 만들기 위해선 1 - 2 - 1 이 성립되어야한다.
    # 1 이라면, 이미 쌓인 스택이 2개 이상, [-1] == 2 and [-2] == 1 인 경우 샌드위치 가능

    for num in nums:
        if num == 1 and len(stack) >= 2 and stack[-1] == 2 and stack[-2] == 1:
            answer += 1
            stack.pop()
            stack.pop()

        else:
            stack.append(num)

    return answer


print(solution([1, 1, 1, 2, 1, 1, 2, 1, 2, 1]))
print(solution([2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1]))
print(solution([1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1]))
print(solution([2, 1, 1, 1, 2, 1, 2]))
print(solution([1, 1, 1, 1, 1, 1, 1]))
