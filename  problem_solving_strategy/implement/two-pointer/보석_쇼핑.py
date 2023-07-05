def solution(gems):
    kind = len(set(gems))
    size = len(gems)

    # 전체 구간
    # 일종의 최대값 설정, 이 구간보다 작은 구간이 있다면 갱신
    answer = [0, size - 1]
    start, end = 0, 0

    # 1번 진열대의 보석을 미리 dic 에 추가
    gem_dic = {gems[0]: 1}

    while end < size:
        # 보석 딕셔너리에 모든 종류의 보석이 아직 없다면
        if len(gem_dic) < kind:
            end += 1

            # end 값이 리스트 끝까지 갔다면
            if end == size:
                break

            gem_dic[gems[end]] = gem_dic.get(gems[end], 0) + 1

        # 보석 딕셔너리에 모든 종류의 보석이 담겼다면
        else:
            # 저장된 구간보다 현재 구간 길이가 더 짧다면 갱신
            if (end - start + 1) < (answer[1] - answer[0] + 1):
                answer = [start, end]

            if gem_dic[gems[start]] == 1:
                del gem_dic[gems[start]]

            else:
                gem_dic[gems[start]] -= 1

            start += 1

    answer[0] += 1
    answer[1] += 1

    return answer


# 진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아 구매
# 가장 짧은 구간이 여러 개라면, 시작 진열대 번호가 가장 작은 구간을 return

#  1     2    3     4     5      6       7      8
# 다이아, 루비, 루비, 다이아, 다이아, 에메랄드, 사파이어, 다이아

# 3 ~ 7 번 구간까지 보석을 모두 구매한다면 모든 종류의 보석을 적어도 1개 이상 포함한다.

# "DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE"
#        "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE"
#                "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE"

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))





# 다이아, 루비, 루비, 다이아, 다이아, 에메랄드, 사파이어, 다이아

# key       value
# 다이아        F
# 루비         F
# 에메랄드      F
# 사파이어      F





# 'AA', 'AB', 'AC', 'AA', 'AC'
    # 'AA', 'AB', 'AC' 세 종류의 보석
    # 1 ~ 3 구간

# XYZ, XYZ, XYZ
    #  한 종류의 보석
    # 1 ~ 1 구간

# ZZZ, YYY, NNNN, YYY, BBB
    # ZZZ, YYY, NNNN, BBB 네 종류의 보석
    # 1 ~ 5 구간


    # ZZZ   # False -> lt 확인 -> 포함되지 않은 보석인 경우니 True 로 변경 -> rt += 1
    # YYY   # False -> rt 확인 -> 포함되지 않은 보석인 경우니 True 로 변경 -> rt += 1
    # NNNN  # False -> rt 확인 -> 포함되지 않은 보석인 경우니 True 로 변경 -> rt += 1
    # BBB   # False