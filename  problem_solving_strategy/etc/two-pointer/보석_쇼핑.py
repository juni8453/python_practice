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

            # start 위치의 보석 개수가 현재 딕셔너리에 여러 개인지 확인
            # 보석이 여러 개라면 뒤에 존재한다는 소리니까 start 를 오른쪽으로 한 칸 이동
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

# print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
# print(solution(["AA", "AB", "AC", "AA", "AC"]))
# print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(['A', 'A', 'A', 'B', 'B', 'C', 'C', 'B', 'A']))
