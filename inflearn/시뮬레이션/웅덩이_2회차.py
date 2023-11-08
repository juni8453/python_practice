def solution(nums):
    answer = 0
    n = len(nums)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i in range(n):
        for j in range(n):
            cur = nums[i][j]
            d_check_count = 0

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                # 격자 넘어가면 1000 이니 +1
                # 아 사실 격자 체크할 필요가 없구나;;
                if not (0 <= nx < n and 0 <= ny < n):
                    d_check_count += 1

                # 격자 내 있으면 현재 격자의 값보다 큰 값인지 확인 후 +1
                elif cur < nums[nx][ny]:
                    d_check_count += 1

            if d_check_count == 4:
                answer += 1

    return answer


print(solution([
    [10, 20, 50, 30, 20],
    [20, 30, 50, 70, 90],
    [10, 15, 25, 80, 35],
    [25, 35, 40, 55, 80],
    [30, 20, 35, 40, 90]
]))

print(solution([
    [80, 25, 10, 65, 100],
    [20, 10, 32, 70, 33],
    [45, 10, 88, 9, 90],
    [10, 32, 10, 55, 66],
    [10, 84, 65, 88, 99]
]))

print(solution([
    [33, 22, 55, 65, 55],
    [55, 88, 99, 12, 19],
    [18, 33, 25, 57, 77],
    [46, 78, 54, 55, 99],
    [33, 25, 47, 85, 17]
]))
