def solution(participant, completion):
    answer = ''
    p_dict = dict()

    for p in participant:
        # p 라는 key 가 이미 p_dict 에 있다면 기존 value 에서 1 추가
        if p in p_dict:
            p_dict[p] += 1

        else:
            p_dict[p] = 1

    # completion 을 순회하면서 맞는 key 값을 찾아 value 를 -1
    for c in completion:
        if c in p_dict: # 없어도 되는 로직
            p_dict[c] -= 1

    # p_dict 에서 value 가 1인 key 추출
    for k, v in p_dict.items():
        if v > 0:
            answer = k

    return answer


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["mislav", "stanko", "mislav", "ana"],
               ["stanko", "ana", "mislav"]))


# 책 풀이
def solution_book(participant, completion):
    answer = dict()

    for i in participant:
        answer[i] = answer.get(i, 0) + 1

    for j in completion:
        answer[j] -= 1

    for k in answer:
        # value 가 정수형이니 0 == False, 1 == True
        if answer[k]:
            return k


print(solution_book(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution_book(["mislav", "stanko", "mislav", "ana"],
               ["stanko", "ana", "mislav"]))