def solution(string):
    stack = []

    for s in string:
        if s == '#':
            stack.pop()

        else:
            stack.append(s)

    return ''.join(stack)


print(solution("abc##ec#ab"))
print(solution("ke"))