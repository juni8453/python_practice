def solution(moves):
    answer = [0, 0]
    R = (0, 1)
    D = (1, 0)
    L = (0, -1)
    U = (-1, 0)

    for move in moves:
        if move == 'R':
            answer[1] += 1

        if move == 'D':
            answer[0] += 1

        if move == 'L':
            answer[1] -= 1

        if move == 'U':
            answer[0] -= 1

    return answer


print(solution('RRRDDDLU'))
print(solution('DDDRRRDDLL'))
print(solution('RRRRRRDDDDDDUULLL'))
print(solution('RRRRDDDRRDDLLUU'))