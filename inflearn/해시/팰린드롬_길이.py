from collections import defaultdict

# 홀수 빈도수 알파벳은 하나까진 사용가능하다
    # 즉, 전체 길이 - 홀수 빈도수 알파벳 개수 + 1
# 홀수 빈도수 알파벳이 없다면 바로 return

def solution(string):
    answer = len(string)
    count = 0
    s_dic = defaultdict(int)
    for s in string:
        s_dic[s] += 1

    print(s_dic)

    for value in s_dic.values():
        if value % 2 != 0:
            count += 1

    if count == 0:
        return answer

    return answer - count + 1


print(solution("abcbbbccaaeee"))
print(solution("aabbccddee"))
print(solution("fgfgabtetaaaetytceefcecekefefkccckbsgaafffg"))