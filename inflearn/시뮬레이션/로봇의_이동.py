# 현재 바라보고 있는 방향을 판단
# 전진인지, 회전인지 판단
    # 전진이라면, 현재 방향으로 x,y 값 갱신
    # 회전이라면, 바라보는 방향 갱신


def solution(moves):
    x = y = 0
    answer = [x, y, 3]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dis = [3, 6, 9, 12]

    for move in moves:
        if move == 'G': # 전진
            # 현재 바라보고 있는 방향 판단 후 해당 방향으로 전진
            for i in range(4):
                if answer[2] == dis[i]:
                    x = x + dx[i]
                    y = y + dy[i]
                    answer[0] = x
                    answer[1] = y

        else: # 회전
            if move == 'R': # 오른쪽 90도 회전인 경우
                for i in range(4):
                    if answer[2] == dis[i]:
                        answer[2] = dis[(i + 1) % 4]
                        break

            elif move == 'L': # 왼쪽 90도 회전인 경우
                for i in range(4):
                    if answer[2] == dis[i]:
                        answer[2] = dis[i - 1]
                        break

    return [answer[0], answer[1]]


print(solution('GGGRGGG'))
print(solution('GGRGGG'))
print(solution('GGGGGGGRGGGRGGRGGGLGGG'))
print(solution('GGLLLGLGGG'))