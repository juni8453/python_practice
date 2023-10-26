def solution(n, moves):
    answer = [0, 0]
    dx = [-1, 0, 0, 1]
    dy = [0, 1, -1, 0]
    dir = ['U', 'R', 'L', 'D']

    for move in moves:
        for i in range(4):
            if move == dir[i]:
                nx = answer[0] + dx[i]
                ny = answer[1] + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    answer[0] = nx
                    answer[1] = ny

    return answer


print(solution(5, 'RRRDDDUUUUUUL'))
print(solution(7, 'DDDRRRDDLL'))
print(solution(5, 'RRRRRDDDDDU'))
print(solution(6, 'RRRRDDDRRDDLLUU'))