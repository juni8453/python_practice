from itertools import permutations
import re


def solution(expression):
    answer = -1e15

    # 문자열 수식인 expression 을 연산자를 기준으로 잘라내야한다.
    # [-+*] -> - 거나 + 거나 * 인 문자를 추출해 구분자로 사용한다는 정규표현식 표현법
    # ([-+*]) -> 소괄호를 씌움으로써 구분자 또한 포함시킬 수 있다.
    expression = re.split('([-+*])', expression)

    # 받아온 문자열 수식에서 +,-,* 를 걸러준다.
    operators_tuples = set()
    for ch in expression:
        if ch == '+' or ch == '-' or ch == '*':
            operators_tuples.add(ch)

    # 중복이 제거된 연산자들로 만들어 낼 수 있는 경우의 수(순열)을 구한다.
    operators_tuples = list(permutations(operators_tuples, len(operators_tuples)))

    for operators_tuple in operators_tuples:
        expression_copy = expression.copy()

        # 하나의 경우의 수에서 먼저 계산할 수식을 정해 계산 진행
        for now_op in operators_tuple:
            # 해당 연산자의 계산을 다 끝냈다면 while 을 빠져나와 튜플에 있는 다음 연산자 순위를 따라 계산 진행
            while now_op in expression_copy:
                idx = expression_copy.index(now_op)
                expression_copy[idx - 1] = str(eval(expression_copy[idx - 1] + now_op + expression_copy[idx + 1]))
                del expression_copy[idx:idx + 2]

        answer = max(answer, abs(int(expression_copy[0])))

    return answer


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))


# index() 는 찾아낸 첫 번째 요소만 찾으니 다른 똑같은 요소의 인덱스 위치를 알기 위해선
# 계산된 결과를 계속해서 expression 에 갱신해야한다.