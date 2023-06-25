from collections import deque


def check_word(stand, compare):
    # 한 글자 제외 다른 두 글자가 같아야 함
    count = 0
    for i in range(len(stand)):
        if stand[i] != compare[i]:
            count += 1

    if count > 1:
        return False

    return True


def solution(begin, target, words):
    queue = deque()
    queue.append([begin, 0])
    visited = [False] * len(words)

    while queue:
        current_word, count = queue.popleft() # 'hit' , 0

        if current_word == target:
            return count

        # 사용하지 않은 단어 중 현재 단어와 교환 가능한 단어를 찾아야한다.
        for i in range(len(words)):
            if not visited[i]:
                # 교환이 가능한 단어인 경우 방문 체크
                if check_word(current_word, words[i]):
                    visited[i] = True
                    queue.append([words[i], count + 1])

    return 00


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
