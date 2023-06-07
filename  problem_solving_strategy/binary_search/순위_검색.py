def solution(info, query):
    answer = []

    # [조건]을 만족하는 사람 중 코딩테스트 점수를 X점 이상 받은 사람은 모두 몇 명인가?
    # 지원자가 지원서에 입력한 4가지의 정보와 획득한 코딩테스트 점수를 하나의 문자열로 구성한 값의 배열 info 1 <= info <= 50,000
    # 개발팀이 궁금해하는 문의조건이 문자열 형태로 담긴 배열 query 1 <= query <= 100,000

    # 조건 X점을 만족하는 지원자를 찾는 문제.

    return answer

info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]

# java 로 코딩 테스트를 봤고 backend 를 지원으며, 경력이 junior, 피자를 선택한 100 점 이상의 지원자는 모두 몇 명인가?
query = ["java and backend and junior and pizza 100",
          "python and frontend and senior and chicken 200",
          "cpp and - and senior and pizza 250",
          "- and backend and senior and - 150",
          "- and - and - and chicken 100",
          "- and - and - and - 150"]

# [1, 1, 1, 1, 2, 4]

print(solution(info, query))
