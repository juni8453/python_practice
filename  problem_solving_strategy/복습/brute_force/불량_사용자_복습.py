from itertools import permutations


def check(unit, banned_ids):
    for i in range(len(banned_ids)):
        # 비교할 경우의 수 문자열 길이와 불량 사용자 문자열 길이가 다르면 False
        if len(unit[i]) != len(banned_ids[i]):
            return False

        for j in range(len(unit[i])):
            if banned_ids[i][j] != '*' and unit[i][j] != banned_ids[i][j]:
                return False

    return True


def solution(user_ids, banned_ids):
    answer = []

    # user_id 길이가 8 밖에 안되니까 모든 경우의 수를 만들어서 판단할 수 있다.
    for unit in list(permutations(user_ids, len(banned_ids))):
        # 만들어진 tuple unit 과 불량 사용자 목록을 검사한다.
        if check(unit, banned_ids):
            # 제한 조건 중 제제 아이디 목록이 나열된 순서와 관계없이 아이디 목록의 내용이 동일하다면 같은 것으로 처리한다 라는 조건을
            # 만족시키기 위해 중복을 제거하는 작업이 필요하다.
            if sorted(unit) not in answer:
                answer.append(sorted(unit))

    return len(answer)


user_ids = ['frodo', 'fradi', 'crodo', 'abc123', 'frodoc']
banned_ids = ['fr*d*', 'abc1**']

user_ids2 = ['frodo', 'fradi', 'crodo', 'abc123', 'frodoc']
banned_ids2 = ['*rodo', '*rodo', '******']

user_ids3 = ['frodo', 'fradi', 'crodo', 'abc123', 'frodoc']
banned_ids3 = ['fr*d*', '*rodo', '******', '******']

print(solution(user_ids, banned_ids))
print(solution(user_ids2, banned_ids2))
print(solution(user_ids3, banned_ids3))
