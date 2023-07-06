from collections import defaultdict
from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    answer = []

    # 점수에 따른 모든 경우의 수를 추출 해야한다.
    # javabackendjuniorpizze : [150], java : [150], java backend : [150] ...
    people = defaultdict(list)

    for i in info:
        person = i.split()

        # value 값으로 사용할 점수 추출
        score = int(person.pop())

        # 가장 기초가 되는 조합 먼저 people 딕셔너리에 추가
        people[''.join(person)].append(score)

        # 언어, 직군, 경력, 소울푸드 4가지 경우에 맞는 모든 경우의 수 찾기
        for j in range(4):
            case = list(combinations(person, j))

            # 기초가 되는 조합 제외 모든 경우의 수를 people 딕셔너리에 추가
            for c in case:
                people[''.join(c)].append(score)

    # 즉, javabackendjuniorpizza : ['150'], java : ['150', '80'],  backend : ['150', '260', '80', '50']
    # 이런 식으로 people 딕셔너리가 구성된다.
    print(people)

    # people 딕셔너리의 value(score) 성적을 모두 정렬
    for key in people:
        people[key].sort()

    for q in query:
        q_key = q.split()
        score = int(q_key.pop())
        q_key = ''.join(q_key)
        q_key = q_key.replace('-', '').replace('and', '').replace(' ', '')

        # 질의에서 뽑아온 key = 'javabackendjuniorpizza', score - [100] 라고 가정
        # 해당 key 로 people[key] 검색 시 몇 명이 각 몇 점인지 알 수 있다.
        # 위 예시로는 people 애서 검색했을 때 score - [150] 이란 것을 알 수 있다.
        # 요구사항으로 score - [100] 점 이상 받은 사람이 몇 명인지 알아내야하므로
        # bisect_left 를 사용해 하한선을 알아낸 뒤 전체 길이에서 빼주면 된다.

        # 즉, people[key] : [150] 일 때 bisect_left 은 0 번째로 나오고, 전체 길이는 1이니
        # [100] 점 보다 높은 인원수가 1명이 된다.
        answer.append(len(people[q_key]) - bisect_left(people[q_key], score))

    return answer


info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]

print(solution(info, query))