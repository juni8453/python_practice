# botom-up 풀이
def solution(n):
    # f(n) = f(n-1) + f(n-2)
    # [0, 1, 1, 2, 3, 5 ...]
    dp = [0 for _ in range(n + 1)]
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 2] + dp[i - 1]

    return dp[n] % 1234567

print(solution(3))
print(solution(5))
