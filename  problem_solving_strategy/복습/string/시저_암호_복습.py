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


# 책 풀이

def solution_book(s, n):
    # 문자열은 immutable 하기 때문에 리스트로 변환해서 푼다.
    s = list(s)

    for i in range(len(s)):
        if s[i] == ' ':
            continue

        # s[i] 가 대문자라면 65('A'), s[i] 가 소문자라면 97('a')
        # (현재 글자의 숫자 - 알파벳 처음 위치 + 더해야 할 숫자 ) % 26 + 알파벳 처음 위치
        # 1. 현재 글자가 만약 'b' 고, 1 만큼 밀고 싶다고 가정
        # 2. b 는 알파벳 상 2번째에 위치하는데, 위치를 구하기 위해 b - a = 1(위치)
        # 3. 구한 위치에서 밀고 싶은 수를 더하고 범위를 지키기 위해 알파벳 전체 갯수인 26 만큼 나눈다. -> 1 + 1 % 26 = 2(위치)
        # 4. 즉, 알파벳 순서로 3번째에 있는 숫자임을 알 수 있으므로 아스키 코드 'a' 를 더한 뒤 다시 변환하면 끝 !
        corr = ord('A') if s[i].isupper() else ord('a')
        s[i] = chr(ord(s[i]) - corr + n) % 26 + corr

    return ''.join(s)


print('AB', 1)