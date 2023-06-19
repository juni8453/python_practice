# 시간 초과 완전탐색 풀이

def solution(phone_book):
    answer = True

    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i].startswith(phone_book[j]):
                return False

            if phone_book[j].startswith(phone_book[i]):
                return False

    return answer


# print(solution(["119", "97674223", "1195524421"]))
# print(solution(["123","456","789"]))
# print(solution(["12","123","1235","567","88"]))


# sorting 을 활용한 풀이
def solution2(phone_book):
    answer = True

    # 문자열 사전 순으로 정렬하면 뒷 원소가 앞 원소의 접두사 일 수 없고, 굳이 하나의 문자열을 기준으로 모든 것을 비교할 필요가 없어진다.
    # 즉, 인접한 두 원소만 비교하면 됨.
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False

    return answer


# hash 을 활용한 풀이
def solution3(phone_book):
    answer = True

    phone_dict = dict()
    for p in phone_book:
        phone_dict[p] = 1

    # 만약 '6789' 라면, '6', '67', '678' 이 접두어가 될 수 있다.
    # 따라서 하나씩 떼어내 pre_str 을 채워주면서 딕셔너리에 접두어가 있는지 찾는다 (자기 자신은 제외한다)
    for number in phone_book:
        pre_str = ''
        for n in number:
            pre_str = ''.join([pre_str, n])

            if pre_str in phone_dict and pre_str != number:
                return False

    return answer

print(solution3(["119", "97674223", "1195524421"]))
print(solution3(["123","456","789"]))
print(solution3(["12","123","1235","567","88"]))