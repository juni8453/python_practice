def solution(s, n):
    answer = []

    # 문자 -> 숫자 ord()
    # 숫자 -> 문자 chr()

    for alpa in s:
        ascii_code = ord(alpa)

        if ascii_code == 32:
            answer.append(' ')

        # 대문자인 경우 밀었을 때 90 이 넘는다면 -26
        if alpa.isupper():
            if ascii_code + n > 90:
                moved_alpa = chr(ascii_code + n - 26)
                answer.append(moved_alpa)

            else:
                moved_alpa = chr(ascii_code + n)
                answer.append(moved_alpa)

        # 소문자인 경우 밀었을 때 122 가 넘는다면 -26
        elif alpa.islower():
            if ascii_code + n > 122:
                moved_alpa = chr(ascii_code + n - 26)
                answer.append(moved_alpa)

            else:
                moved_alpa = chr(ascii_code + n)
                answer.append(moved_alpa)

    return ''.join(answer)

print(solution('AB', 1))
print(solution('z', 1))
print(solution('a B z', 4))

# 문자열 s 를 n 만큼 민 암호문을 만드는 함수를 구현