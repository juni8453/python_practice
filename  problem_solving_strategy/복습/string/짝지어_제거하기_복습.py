def solution(s):
    answer = 0
    stack = []

    for i in s:
        if len(stack) == 0: # 첫 소문자는 넣고 continue
            stack.append(i)
            continue

        if i == stack[-1]: # 확인할 알파벳과 stack 의 pop 이 같다면 추가하지 말고 지우기
            stack.pop()

        else: # 다르댜면 stack 에 추가
            stack.append(i)

    # stack 이 비었다면, answer 1 로 갱신
    if len(stack) == 0:
        answer = 1

    return answer


print(solution('baabaa'))
