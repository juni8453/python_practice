def recursion(now_word, target_word, word_list):
    vowel = ['A', 'E', 'I', 'O', 'U']

    if now_word == target_word:
        return

    if len(now_word) == 5:
        return

    for i in range(5):
        new_word = now_word + vowel[i]
        word_list.append(new_word)
        recursion(new_word, target_word, word_list)


def solution(target_word):
    word_list = []

    recursion('', target_word, word_list)

    # 모음 사전에 단어를 기록했기 때문에 몇 번째 인덱스인지 찾는다.
    return word_list.index(target_word) + 1


print(solution("AAAAE")) # 6
print(solution("I")) # 1563

# word 는 단어 사전의 몇 번째 단어인가 ?