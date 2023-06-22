from collections import deque


def solution(protected_order, want_orders):
    answer = 0

    # deque 를 활용해 미리 순서를 셋팅하고 순서대로 온다면 popleft() 하면서 진행
    # 순서대로 오지 않으면 그대로 break

    for want_order in want_orders:
        queue = deque(protected_order[:])

        for one_skill in want_order:
            # protected_order 에 있는 스킬이지만
            # 순서가 안맞으면 바로 다름 want_order 로 넘어감
            # protected_order 에 없는 스킬 (힐링 등) 이라면 계속 진행
            if one_skill in protected_order and one_skill != queue.popleft():
                break

        # for 문이 정상동작했다면 가능한 스킬트리이므로 answer 증가
        else:
            answer += 1

    return answer


# 스파크 -> 라이트닝 볼트 -> 썬더
# 스파크 -> 힐링 -> 라이트닝 볼트 -> 썬더는 가능
# 썬더 -> 스파크 or 라이트닝 볼트 -> 스파크 -> 힐링 -> 썬더 불가능
# 즉, 스킬트리가 따로 없는 스킬은 어느때나 배울 수 있고, 스킬트리가 있는 스킬은 항상 스킬트리 순서대로

# skill : 'CBD', C -> B -> D 순서로 배워야함
# 'BACDE' -> C 이후 B 를 배워야하지만 B 를 먼저 배웠으니 불가능한 스킬트리

# 어짜피 protected_skill_order 에 포함되지 않는 다른 '힐' 과 같은 스킬은 순서를 따질 필요가
# 없고, deque 를 사용해서 for 문을 모두 돌리는데 성공한다면 answer 값 증가


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
print(solution("CBD", ["AEF"]))

# skills 의 순서에 맞게 스킬트리를 찍어줘야한다.
