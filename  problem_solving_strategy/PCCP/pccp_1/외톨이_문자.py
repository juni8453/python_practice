def solution(string):
    answer = ''
    prev = ''
    alpa_dic = dict()

    for s in string:
        if s not in alpa_dic:
            alpa_dic[s] = False

        elif s in alpa_dic and prev != s:
            alpa_dic[s] = True

        prev = s

    keys = []
    for key in alpa_dic:
        if alpa_dic[key]:
            keys.append(key)

    if len(keys) == 0:
        return 'N'

    answer = ''.join(keys)

    return answer


print(solution("eeddee"))
print(solution("string"))
print(solution("edeaaabbccd"))