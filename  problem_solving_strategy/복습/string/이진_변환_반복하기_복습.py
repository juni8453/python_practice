def solution(s):
    # x 진법 -> 10진법
    # int(<해당 진법 문자열>, <해당 진법>)

    # 10 진법 -> 2, 8, 16진법
    # bin(), oct(), hex()

    # 10 진법 -> x 진법
    # 따로 구현 필요

    call_func_count = 0
    removed_zero = 0

    while s != '1':
        call_func_count += 1
        s_len = len(s)

        # x 의 모든 0을 제거한다.
        # == 1의 개수를 세는 것과 동일
        now_s = list(s)
        c = now_s.count('1')
        removed_zero += (s_len - c)

        # c 를 이진 변환한다.
        s = bin(c)[2:]

    return [call_func_count, removed_zero]


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))
