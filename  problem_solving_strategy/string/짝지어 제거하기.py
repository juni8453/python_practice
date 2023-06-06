def solution(s):
    answer = -1

    # 제거 후 s 가 갱신되어야한다.
    # 제거 작업을 마친 후 길이가 0이 아니라면 -1 을 return
    # 10^6 이니까 O(n^2) 이하의 알고리즘을 짜야한다.
    # 뿌요뿌요를 생각하면 쉬움

    check_stack = []

    for i in s:
        if len(check_stack) == 0:
            check_stack.append(i)
            continue

        stand = check_stack[-1]
        if stand != i:
            check_stack.append(i)

        else:
            check_stack.pop()

    if len(check_stack) == 0:
        answer = 1
    else:
        answer = 0

    return answer