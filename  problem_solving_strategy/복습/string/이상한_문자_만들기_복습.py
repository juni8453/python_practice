# 내 풀이

def solution(s):
    answer = []

    # 공백 기준으로 단어를 나눠 새로운 s 리스트를 만든다.
    s = s.split(' ')

    for i, word in enumerate(s):
        for word_idx, c in enumerate(word):
            if word_idx % 2 == 0:
                # 대문자로 변환
                answer.append(c.upper())

            else:
                # 소문자로 변환
                answer.append(c.lower())

        if i != len(s) - 1:
            answer.append(' ')

    return ''.join(answer)


print(solution('try hello world'))

# 각 단어의 짝수 번째 알파벳은 대문자로, 홀수 번째 알파벳은 소문자로 바꾼 문자열을 반환
# try -> TrY
# hello -> HeLlO
# world -> WoRlD

# 책 풀이

def solution_book(s):
    s = list(s)

    # 공백을 감지하고 단어의 인덱스가 짝수인지 홀수인지 판단하는 두 가지 일을 하는 변수
    count = 0

    for i in range(len(s)):
        if s[i] == ' ':
            count = 0
            continue

        s[i] = s[i].upper() if count % 2 == 0 else s[i].lower()
        count += 1

    return ''.join(s)


print(solution_book('try hello world'))