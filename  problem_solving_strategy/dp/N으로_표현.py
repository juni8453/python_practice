def solution(n, target):
    dp = [set() for _ in range(9)]

    for i in range(1, 9):
        case = dp[i]
        case.add(int(str(n) * i))

        for j in range(1, i):
            for k in dp[j]:
                for l in dp[i - j]:
                    case.add(k + l)
                    case.add(k - l)
                    case.add(k * l)

                    if k != 0 and l != 0:
                        case.add(k // l)

        if target in case:
            return i

    return -1


print(solution(5, 12))