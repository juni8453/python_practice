from collections import defaultdict


def solution(n, results):
    answer = 0

    total = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        total[i][i] = -1

    for result in results:
        total[result[0] - 1][result[1] - 1] = 'win'
        total[result[1] - 1][result[0] - 1] = 'lose'

    # 플로이드 - 와샬 적용
    # i 번 선수와 j 번 선수가 경기를 진행한다고 했을 때,
    # i 번 선수와 k 번 선수, k 번 선수와 j 번 선수가 경기한 이력을 확인
    # 만약 i 번 선수가 k 번 선수를 이겼고, k 번 선수가 j 번 선수를 이겼다면
    # i 번 선수는 j 번 선수에게 승리한다.

    # 만약 i 번 선수가 k 번 선수에게 졌고, k 번 선수가 j 번 선수에게 졌으면
    # i 번 선수는 j 번 선수에게 패배한다.
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if total[i][k] == 'win' and total[k][j] == 'win':
                    total[i][j] = 'win'

                elif total[i][k] == 'lose' and total[k][j] == 'lose':
                    total[i][j] = 'lose'

    for i in range(n):
        if 0 not in total[i]:
            answer += 1

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))


# 선수 번호 : 1 ~ n
# A 선수가 B 선수보다 실력이 좋다면 A 는 B 를 항상 이긴다.

# 정확하게 순위를 매길 수 있는 선수란?
# n 명에서 다른 선수들과 모든 매치업을 마친 데이터가 있는 선수
# 예를 들어, 100 명이라면 2 명씩 붙는거니 100c2 -> 4,950 개의 데이터가 있어야 순위를 매길 수 있는 선수가 된다.