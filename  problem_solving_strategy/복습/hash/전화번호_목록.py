def solution(phone_book):
    phone_dict = dict()

    for number in phone_book:
        phone_dict[number] = 1

    # 전화번호 하나를 선택해서 자신이 가질 수 있는 접두어를 하니씩 만들어준다.
    # 접두어가 딕셔너리에 있다면 바로 False 반환
    for number in phone_book:
        pre = ''

        for n in number:
            # 접두어 만들기
            pre = ''.join([pre, n])

            # 만들어진 접두어가 딕셔너리에 있고, 그게 자신이 아닌 경우라면
            if pre in phone_dict and pre != number:
                return False

    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))
