def search(cur_x, cur_y, n, nums):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(4):
        nx = cur_x + dx[i]
        ny = cur_y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if nums[cur_x][cur_y] >= nums[nx][ny]:
                return 0
    return 1


def solution(nums):
    answer = 0
    n = len(nums)

    for i in range(n):
        for j in range(n):
            count = search(i, j, n, nums)
            answer += count

    return answer


print(solution([[10, 20, 50, 30, 20],
                [20, 30, 50, 70, 90],
                [10, 15, 25, 80, 35],
                [25, 35, 40, 55, 80],
                [30, 20, 35, 40, 90]]))

print(solution([[80, 25, 10, 65, 100],
                [20, 10, 32, 70, 3],
                [45, 10, 88, 9, 90],
                [10, 35, 10, 55, 66],
                [10, 84, 65, 88, 99]]))

print(solution([[33, 22, 55, 65, 55],
                [55, 88, 99, 12, 19],
                [18, 33, 25, 57, 77],
                [46, 78, 54, 55, 99],
                [33, 25, 47, 85, 17]]))
