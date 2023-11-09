def solution(targets):
    answer = 0
    targets.sort(key = lambda x: [x[1]])
    # print(targets)

    # 현재 요격 미사일의 조준점
    shooting_point = 0

    for start, end in targets:
        # print(shoting_point)
        if shooting_point <= start: # 미사일이 곂치지 않는 경우
            answer += 1 # 한 발 발싸
            shooting_point = end # 조준점을 다음 미사일 끝으로 수정

        # 미사일이 곂치는 경우 현재 조준점에 고정한 뒤 다음 미사일을 확인한다.
        # else 없이 넘어가면 될 듯

    return answer