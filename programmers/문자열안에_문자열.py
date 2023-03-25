def solution(str1, str2):
  if str2 in str1:
    return 1

  return 2

# 있다면 1, 없다면 2 반환
print(solution('ab6CDE443fgh22iJKlmn1o', '6CD'))
print(solution('ppprrrogrammers', 'ppppp'))
