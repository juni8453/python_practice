def solution(numbers, hand):
    answer = ''
    dis = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }

    left_x1 = dis['*'][0]
    left_y1 = dis['*'][1]
    right_x1 = dis['#'][0]
    right_y1 = dis['#'][1]

    for number in numbers:
        # 1, 4, 7 인 경우 (왼손 사용)
        if number == 1 or number == 4 or number == 7:
            answer += 'L'
            left_x1 = dis[number][0]
            left_y1 = dis[number][1]

        # 3, 6, 9 인 경우 (오른손 사용)
        elif number == 3 or number == 6 or number == 9:
            answer += 'R'
            right_x1 = dis[number][0]
            right_y1 = dis[number][1]

        # 2, 5, 8, 0 인 경우 (거리 계산 필요)
        elif number == 2 or number == 5 or number == 8 or number == 0:
            # 공식) (x2 - x1)^2 + (y2 - y1)^2
            # x2, y2 는 타겟 키패드 위치
            # |x1-x2|+|y1-y2|
            x2, y2 = dis[number]
            left_interval = abs(left_x1 - x2) + abs(left_y1 - y2)
            right_interval = abs(right_x1 - x2) + abs(right_y1 - y2)

            # 왼손이 더 멀다면
            if left_interval > right_interval:
                answer += 'R'
                right_x1 = dis[number][0]
                right_y1 = dis[number][1]

            # 오른손이 더 멀다면
            elif left_interval < right_interval:
                answer += 'L'
                left_x1 = dis[number][0]
                left_y1 = dis[number][1]

            # 길이 차이가 같다면
            elif left_interval == right_interval:
                if hand == 'right':
                    answer += 'R'
                    right_x1 = dis[number][0]
                    right_y1 = dis[number][1]

                elif hand == 'left':
                    answer += 'L'
                    left_x1 = dis[number][0]
                    left_y1 = dis[number][1]

    return answer

# 1  2  3
# 4  5  6
# 7  8  9
# *  0  #
#(왼)  (오) 시작지점

# 1, 4, 7 -> 왼손
# 3, 6, 9 -> 오른손
# 2, 5, 8, 0 -> 두 손의 위치에서 더 가까운 손 사용
# 만약 목표 키패드까지의 거리가 같다면 오른손잡이는 오른손, 왼손잡이는 왼손 사용

# numbers 에 따라 왼손, 오른손을 움직이면서 (위치도 저장) answer 배열에 저장하고
# 2, 5, 8, 0 이 나오면 hand 에 따라 알맞은 손을 움직인다.
# 거리를 구해야하니까 2중 배열을 사용하면 될듯