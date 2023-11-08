# 최초 방향이 동, 90도 시계방향 회전에 맞춰 동, 남, 서, 북 순으로 설정
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def solution(moves):
    # [최초 행, 최초 열, 최초 방향(dx[0], dy[0]]
    robot_info = [0, 0, 0]

    for move in moves:
        if move == 'G':
            robot_info[0] += dx[robot_info[2]]
            robot_info[1] += dy[robot_info[2]]

        elif move == 'R':
            robot_info[2] = (robot_info[2] + 1) % 4

        elif move == 'L':
            robot_info[2] = (robot_info[2] + 3) % 4

    return [robot_info[0], robot_info[1]]


print(solution('GGGRGGG'))
print(solution('GGRGGG'))
print(solution('GGGGGGGRGGGRGGRGGGLGGG'))
print(solution('GGLLLGLGGG'))