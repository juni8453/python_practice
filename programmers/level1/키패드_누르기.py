import math

def solution(numbers, hand):
    answer = ''
    pad = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        '*': [3, 0], 0: [3, 1], '#': [3, 2]
    }

    left_start = pad['*']
    right_start = pad['#']

    for i in numbers:
        now = pad[i]

        # i가 [1, 4, 7] 중 하나라면, 왼손
        if i in [1, 4, 7]:
            answer += 'L'
            left_start = now

        # i가 [3, 6, 9] 중 하나라면, 오른손
        elif i in [3, 6, 9]:
            answer += 'R'
            right_start = now

        else:
            l_x, l_y = left_start # 현재 왼손 위치
            r_x, r_y = right_start # 현재 오른손 위치
            target_x, target_y = pad.get(i) # 타겟 키패드 위치

            # 거리 구하기
            l_dis = math.ceil(math.sqrt(math.pow(target_x - l_x, 2) + math.pow(target_y - l_y, 2)))
            r_dis = math.ceil(math.sqrt(math.pow(target_x - r_x, 2) + math.pow(target_y - r_y, 2)))

            # 완손이 더 멀다면,
            if l_dis > r_dis:
                answer += 'R'
                right_start = now

            # 오른손이 더 멀다면,
            elif r_dis > l_dis:
                answer += 'L'
                left_start = now

            # 왼손, 오른손 거리 차가 같다면,
            elif r_dis == l_dis:
                if hand == 'left':
                    answer += 'L'
                    left_start = now

                elif hand == 'right':
                    answer += 'R'
                    right_start = now

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
