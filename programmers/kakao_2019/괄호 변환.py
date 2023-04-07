def slice_str(str):
  correct = True
  left = 0
  right = 0
  my_list = []

  for i in range(len(str)):
    if str[i] == '(':
      left += 1
      my_list.append('(')

    # 올바른 괄호가 맞는지 확인한다.
    else:
      right += 1
      if len(my_list) == 0: # 앞에 열린 괄호가 없는 경우
        correct = False

    # ')(' <- 이런 경우라면 correct False 를 반환
    if left == right:
      return str[:i + 1], str[i + 1:], correct

def solution(p):
  # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환
  if len(p) == 0:
    return p

  # 2. 문자열 w 를 두 균형잡힌 문자열 u,v 로 분리
  u, v, correct = slice_str(p)

  # 3. u 가 올바른 괄호 문자열이라면 문자열 v 에 대해 1단계부터 다시 수행하고 결과를 u 에 이어 붙인 후 반환
  if correct:
    return u + solution(v)

  # 4. u 가 올바른 괄호 문자열이 아니라면 빈 문자열에 '('를 붙인다.
  else:
    # v 에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙이고 다시 ')' 를 붙인다.
    answer = '(' + solution(v) + ')'
    # u 의 첫 문자와 마지막 문자를 제거하고 나머지 문자를 거꾸로 뒤집어 붙인다.
    # 그냥 1번 인덱스부터 마지막 전 인덱스까지 괄호를 확인해 뒤집는 방법 사용
    for i in range(1, len(u) - 1):
      if u[i] == '(':
        answer += ')'
      else:
        answer += '('

  return answer

print(solution('()'))
print(solution(')(())()(())('))
print(solution('()))((()'))