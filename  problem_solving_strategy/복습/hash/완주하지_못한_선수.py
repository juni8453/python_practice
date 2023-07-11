def solution(participant, completion):
    answer = ''
    p_dict = dict()

    for name in participant:
        p_dict[name] = p_dict.get(name, 0) + 1

    for name in completion:
        if name in p_dict:
            p_dict[name] -= 1

    for name, count in p_dict.items():
        if count > 0:
            answer = name

    return answer


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))