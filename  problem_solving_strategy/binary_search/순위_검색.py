# 효용성 테스트 통과 X 풀이
# [조건]을 만족하는 사람 중 코딩테스트 점수를 X점 이상 받은 사람은 모두 몇 명인가?
# 지원자가 지원서에 입력한 4가지의 정보와 획득한 코딩테스트 점수를 하나의 문자열로 구성한 값의 배열 info 1 <= info <= 50,000
# 개발팀이 궁금해하는 문의조건이 문자열 형태로 담긴 배열 query 1 <= query <= 100,000

# 조건 X점을 만족하는 지원자를 찾는 문제.

def solution(info, query):
    data = [i.split() for i in info]
    queries = []

    for q in query:
        q = q.split()

        # and 는 탐색할 필요가 없으므로 지우고 queries 리스트에 새로 넣는다.
        for _ in range(3):
            q.remove('and')
        queries.append(q)

    answer = [0] * len(query)

    # 이제 data 와 queries 를 맞췄으니 3중 반복문을 사용해서 알맞은 지원자가 몇 번 호출되었는지 기록을 남긴다.
    for i in range(len(queries)):
        query = queries[i] # query 에 '-' 가 있을 수도 있다.

        for candidate_info in data:
            for j in range(5): # query 와 candidate_info 길이는 5이므로 5만큼 돌면서 확인한다.
                # query 에서 '-' 문자열이 발견되면 비교하지 않고 넘긴다.
                if query[j] == '-':
                    continue

                # 점수를 확인해서 지원자의 점수가 같거나 더 높다면 기록을 남긴다.
                elif j == 4 and int(query[j]) <= int(candidate_info[j]):
                    answer[i] += 1

                # query 와 candidate_info 가 다르다면 다른 candidate_info 를 비교하기 위해 반복문을 종료한다.
                elif query[j] != candidate_info[j]:
                    break

    return answer

info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]

# java 로 코딩 테스트를 봤고 backend 를 지원했으며, 경력이 junior, 피자를 선택한 100 점 이상의 지원자는 모두 몇 명인가?
query = ["java and backend and junior and pizza 100",
          "python and frontend and senior and chicken 200",
          "cpp and - and senior and pizza 250",
          "- and backend and senior and - 150",
          "- and - and - and chicken 100",
          "- and - and - and - 150"]

# [1, 1, 1, 1, 2, 4]

print(solution(info, query))


# 책 풀이
from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def solution_book(info, query):
    answer = []

    # dict() 에 미리 value 값 타입으로 list 를 지정해서 사용
    people = defaultdict(list)

    for i in info:
        person = i.split()
        score = int(person.pop())

        # {'언어 + 직군 + 경력 + 선호음식', '점수'}
        people[''.join(person)].append(score)

        # 언어, 직군, 경력, 선호음식에서 '-'(즉, 생략될 수 있는) 가 사용될 수 있는 모든 경우의 수를 뽑아낸다.
        for j in range(4):
            case = list(combinations(person, j))

            for c in case:
                people[''.join(c)].append(score)

    # 기록한 딕셔터리의 성적 데이터를 모두 정렬 (이진 탐색을 위함)
    for i in people:
        people[i].sort()

    print('현재 people 딕셔너리:', people)

    # people 딕셔너리 key 값으로 조건, value 값으로 성적을 담았으니 질의 리스트를 추출, key 값으로 만들고 people 딕셔너리에서 사용한다.
    # 이 때 bisect_left 를 활용해
    for i in query:
        key = i.split()
        score = int(key.pop()) # 점수 추출

        key = ''.join(key)
        key = key.replace('and', '').replace(' ', '').replace('-', '')

        print('현재 people[key]:', people[key])
        print('현재 score:', score)
        print(bisect_left(people[key], score))

        # bisect_left(<리스트>, <찾을 원소>)
        # 전체 길이에서 score 보다 작은 값의 인덱스를 빼주면, 해당 score 보다 더 큰 값이 몇 개가 있는지 알아낼 수 있다.
        # 예를 들어 people[key] = [80, 150], score = 100 이라고 하면,
        # 전체 길이는 2, 100 이 들어갈 수 있는 index 는 1 즉, 서로 빼면 100 보다 더 큰 경우는 하나인 걸 알 수 있다.
        answer.append(len(people[key]) - bisect_left(people[key], score))

    return answer

info = ["java and junior pizza 150",
"python frontend senior chicken 210",
"python frontend senior chicken 150",
"cpp backend senior pizza 260",
"java backend junior chicken 80",
"python backend senior chicken 50"]

# java 로 코딩 테스트를 봤고 backend 를 지원했으며, 경력이 junior, 피자를 선택한 100 점 이상의 지원자는 모두 몇 명인가?
query = ["java and backend and junior and pizza 100",
"python and frontend and senior and chicken 200",
"cpp and - and senior and pizza 250",
"- and backend and senior and - 150",
"- and - and - and chicken 100",
"- and - and - and - 150"]

print(solution_book(info, query))