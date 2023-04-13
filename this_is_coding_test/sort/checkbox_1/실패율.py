def solution(N, stages):
    answer = []

    # N = 총 스테이지 개수
    # stages[i] = i 번째 유저가 어느 스테이지에 머무르고 있는지 나타냄 (3 이라면, 해당 유저는 3 스테이지를 아직 클리어하지 못한 상황)
    # 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 유저 수 / 스테이지에 도달한 플레이어 수

    length = len(stages) # 스테이지에 도달한 플레이어 수
    for i in range(1, N + 1):
        cur_stage_stop_user = stages.count(i)

        if length == 0:
            fail = 0

        else:
            # 실패율 계산
            fail = cur_stage_stop_user / length

        answer.append((i, fail)) # 현재 스테이지의 실패율
        length -= cur_stage_stop_user

    # 실패율이 높은 스테이지부터 내림차순
    answer = sorted(answer, key = lambda x: x[1], reverse=True)
    answer = [i[0] for i in answer]

    return answer

print(solution(5, [3,1,2,6,2,4,3,3]))