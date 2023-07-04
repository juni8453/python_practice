# 괄호 문자열 p 를 u, v 로 쪼개는 함수
def p_divide(p):
    l_cnt = 0
    r_cnt = 0

    # 개수만 맞으면 되니까 어렵게 판단할 필요 X
    for i in range(len(p)):
        if p[i] == '(':
            l_cnt += 1

        elif p[i] == ')':
            r_cnt += 1

        if l_cnt == r_cnt:
            u = p[:i + 1]
            v = p[i + 1:]
            break

    return u, v


# 괄호 문자열 u 가 올바른 괄호인지 체크하는 함수
# 열린 괄호부터 시작하는지? 뿌요뿌요 했을 때 Stack 에 값이 없다면 올바른 괄호
def right_check(u):
    if u[0] == ')':
        return False

    stack = []
    for i in range(len(u)):
        if u[i] == '(':
            stack.append(u[i])

        elif stack[-1] == '(' and u[i] == ')':
            stack.pop()

        elif len(stack) == 0 and u[i] == ')':
            return False

    if len(stack) != 0:
        return False

    return True

def solution(p):
    answer = ''

    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환한다.
    if len(p) == 0:
        return p

    # 2. 문자열 w 를 균형잡힌 괄호 u, v 로 분리한다.
    # u 는 균형잡힌 괄호이며 v 는 빈 문자열이 될 수 있다.
    u, v = p_divide(p)

    # 3. 문자열 u 가 올바른 괄호라면 문자열 v 에 대해 1단계부터 다시 수행한다.
    if right_check(u):
        # 3-1. 수행 결과를 u 에 이어 붙힌 후 반환한다.
        return u + solution(v)

    # 4. 문자열 u 가 올바른 괄호가 아니라면,
    elif not right_check(u):
        # 4-1. 빈 문자열에 첫 번째 문자로 '(' 를 붙인다.
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙인다.
        # 4-3. ')' 를 다시 붙인다.
        answer = '(' + solution(v) + ')'

        # 4-4. u 의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어 뒤에 붙인다.
        u = u[1:len(u) - 1]
        new_u = ''

        for i in range(len(u)):
            if u[i] == '(':
                new_u += ')'
            else:
                new_u += '('

        answer += new_u

        # 4-5. 생성된 문자열을 반환한다.
        return answer

    return ''


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))