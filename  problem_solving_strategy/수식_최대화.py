import re
from itertools import permutations

def solution(expression):
    # 연산자에 따른 경우의 수를 따져야하기 떄문에 먼저 문자와 연산자로 나누는 작업이 필요하다.
    expression = re.split('([-+*])', expression)

    # permutations 를 활용해 모든 연산 경우를 따질 수 있다.
    operators = list(permutations(['-', '+', '*'], 3))

    # 한 번의 operators 를 선택
    # ex) ('-', '+', '*') -> '-' 연산부터 시작 -> '-' index 번호를 찾아서 앞, 뒤 인덱스 원소를 해당 연산에 맞게 계산한다.
    answers = []
    for operator in operators:
        # 한 바퀴 연산이 끝나면 똑같은 expression 객체로 다른 연산을 해야하므로 계속해서 배열 복사 후 사용
        new_expression = expression[:]

        for op in operator:
            # 선택된 연산을 계속해서 찾고 위에 적어놓은 계산 실시
            while op in new_expression:
                idx = new_expression.index(op)
                new_expression[idx - 1] = str(eval(new_expression[idx - 1] + op + new_expression[idx + 1]))
                del new_expression[idx:idx + 2]

        answers.append(abs(int(new_expression[0])))

    return max(answers)

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))