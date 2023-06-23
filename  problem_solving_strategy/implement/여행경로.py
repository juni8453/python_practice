def solution(tickets):
    answer = []

    routes = dict()
    for start, end in tickets:
        routes[start] = routes.get(start, []) + [end]

    # pop() 을 활용해 Value List 맨 뒤의 값부터 가져오기 위해 역순 정렬
    # 사전순 정렬 후 pop(0) 을 사용해도 되지만 시간 복잡도 상 불리함
    for key in routes:
        routes[key].sort(reverse=True)

    # stack 에 항공권을 차례로 쌓는다.
    stack = ['ICN']

    while stack:
        current_location = stack[-1]

        # 현재 있는 곳에서 다른 곳으로 갈 티켓이 없거나(= Key 가 존재하지 않다는 뜻),
        # 현재 있는 곳에서 다른 곳으로 갈 티켓이 없다면,
        # 모든 티켓을 소진했으므로 stack 에서 answer 로 값을 옮긴다.
        if current_location not in routes or len(routes[current_location]) == 0:
            answer.append(stack.pop())

        else:
            stack.append(routes[current_location].pop())

    # pop() 에 의해 역순으로 값이 삽입되기 때문에 배열을 거꾸로 뒤집어 반환
    return answer[::-1]


# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))