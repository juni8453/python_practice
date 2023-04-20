def solution(s):
    answer = ''
    answer_list = []
    count = 0

    for text in s:
        if text == ' ': # 공백을 만나면 count 초기화
            answer_list.append(' ')
            count = 0
            continue

        else:
            if count % 2 == 0:
                answer_list.append(text.upper())
                count += 1

            elif count % 2 != 0:
                answer_list.append(text.lower())
                count += 1

    return ''.join(answer_list)