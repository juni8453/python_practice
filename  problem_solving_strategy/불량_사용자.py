# 순서를 따지지 않으므로 permutations 순열을 사용
from itertools import permutations

def check(unit, banned_id):
    for i in range(len(banned_id)):
        if len(unit[i]) != len(banned_id[i]):
            return False

        # 서로 문자가 달라도 * 이라면 괜찮은데 * 도 아니라면 False 반환
        for j in range(len(banned_id)):
            if unit[i][j] != banned_id[i][j] and banned_id[i][j] != '*':
                return False

    return True

def solution(user_id, banned_id):
    answer = []

    # 아이디 리스트 길이가 8 이하이므로 모든 경우의 수를 따져서 확인할 수 있다.
    for unit in permutations(user_id, len(banned_id)):
        # unit tuple 과 banned_id 가 동일 -> answer 에 추가
        if check(unit, banned_id):
            if set(unit) not in answer:
                answer.append(set(unit))

    return len(answer)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))

# 1 <= user_id, banned_id <= 8
# banned_id 중 하나는 user_id 중 하나와 매칭된다.
# 같은 user_id 가 중복 제재되는 경우는 없다.
# 제재 아이디 목록을 구현했을 때 아이디들이 나열된 순서와 관계없이 내용이 동일하다면 하나로 간주한다.