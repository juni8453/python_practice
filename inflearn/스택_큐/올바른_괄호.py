# 닫힌 괄호는 스택이 비었을 때 삽입된다면 무조건 NO 반환

def solution(string):
    answer = 'YES'
    stack = []

    for s in string:
        if s == ')':
            if len(stack) == 0:
                return 'NO'

            elif stack[-1] == '(':
                stack.pop()

        elif s == '(':
            stack.append('(')

    return answer if len(stack) == 0 else "NO"


print(solution("((()))()"))
print(solution("(()(()"))
print(solution("()())"))
print(solution("())("))
print(solution("((())))()("))