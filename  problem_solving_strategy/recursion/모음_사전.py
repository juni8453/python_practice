# 첫 번째 풀이
def find(data, p, step):
    if step == 6:
        return

    if p != '':
        data.append(p)

    for c in ['A', 'E', 'I', 'O', 'U']:
        find(data, ''.join([p, c]), step + 1)


def solution(word):
    answer = 0
    data = [] # 모음 사전을 담을 리스트
    find(data, '', 0)

    for i in range(len(data)):
        if data[i] == word:
            answer = i + 1
            break

    return answer


print(solution("AAAAE"))

# -----

# 두 번째 풀이
def solution(word):
    word_list = []
    words = 'AEIOU'

    def dfs(count, word):
        if count == 5:
            return

        for i in range(5):
            word_list.append(word + words[i])
            dfs(count + 1, word + words[i])

    dfs(0, '')

    return word_list.index(word) + 1

print(solution('AAAAE'))