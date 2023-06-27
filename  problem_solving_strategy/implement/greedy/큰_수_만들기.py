def solution(numbers, k):
    stack = []

    for number in numbers:
        # 앞 숫자가 더 작을 경우 계속해서 지워주기 위해 while 사용
        # pop() 은 숫자를 하나 지웠다는 의미니까, k 도 1 감소
        while stack and stack[-1] < number and k > 0:
            stack.pop()
            k -= 1

        stack.append(number)

    return ''.join(stack[:len(stack) - k])


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))