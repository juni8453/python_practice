# 제약 조건
# 1 <= s.length <= 10^4
# -> O(n^2) 으로 플이할 수 없음. (완전탐색 X)
# -> O(nlogn), O(n), O(logn), O(1) 알고리즘으로 풀이
#
# 접근
# 1. 괄호의 짝이 맞아야 한다.
# 2. 소, 중, 대괄호를 구분해서 짝이 맞아야 한다.
# 3. 가장 마지막 괄호가 닫히기 전에 다른 괄호가 닫히면 안된다.

def valid_parentheses(s):
  stack = []
  for parentheses in s:
    if parentheses == "(":
      stack.append(")")
    elif parentheses == "{":
      stack.append("}")
    elif parentheses == "[":
      stack.append("]")

    # 조건문 not 사용 가능
    # stack 이 빈 경우 또는 꺼냈을 떄 paren 가 아니면,
    elif not stack or stack.pop() != parentheses:
      return False
  # stack 이 빈 경우 True 반환
  return not stack


print(valid_parentheses("()"))

