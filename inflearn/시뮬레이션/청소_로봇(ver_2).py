def solution(moves):
    answer = [0, 0]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dir = ['R', 'D', 'L', 'U']

    for move in moves:
        for i in range(4):
            if move == dir[i]:
                answer[0] += dx[i]
                answer[1] += dy[i]
    return answer


print(solution('RRRDDDLU'))
print(solution('DDDRRRDDLL'))
print(solution('RRRRRRDDDDDDUULLL'))
print(solution('RRRRDDDRRDDLLUU'))