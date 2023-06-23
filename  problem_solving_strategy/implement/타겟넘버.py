def solution(numbers, target):
    count = 0

    def dfs(depth, current_sum):
        nonlocal count

        # Base Case
        if depth == len(numbers):
            if current_sum == target:
                count += 1
            return

        # Operation
        dfs(depth + 1, current_sum + numbers[depth])
        dfs(depth + 1, current_sum - numbers[depth])

    # DFS 실행
    dfs(0, 0)

    return count


print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))