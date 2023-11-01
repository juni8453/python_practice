def solution(string):
    stack = []

    for s in string:
        if len(stack) != 0 and stack[-1] == s:
            stack.pop()
            continue
        stack.append(s)

    return ''.join(stack)


print(solution('acbbcaa'))
print(solution('bacccaba'))
print(solution('aabaababbaa'))
print(solution('bcaacccbaabccabbaa'))
print(solution('cacaabbc'))