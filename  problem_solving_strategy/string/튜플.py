def solution(s):
    # 필요없는 중괄호는 삭제하고 나눈다.
    answer_dict = {}
    answer_list = []

    datas = s[2:-2].split('},{')
    datas = sorted(datas, key=lambda x: len(x)) # 집합이 주어졌을 떄 원소 갯수가 작은게 앞으로 오므로 갯수 오름차순 정렬

    for item in datas:
        item = list(map(int, item.split(',')))
        for value in item:
            if value not in answer_dict:
                answer_dict[value] = 1
                answer_list.append(value)

    return answer_list

print(solution(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")))