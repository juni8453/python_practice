def solution(s):
  count_0 = 0
  count_1 = 0

  # 맨 처음 글자 셋팅
  if s[0] == '0':
    count_0 += 1
  else:
    count_1 += 1

  # 두 번쨰 원소부터 리스트를 돌면서 앞 글자와 현재 글자 비교
  # 글자가 다를 때 연속이 끝났다는 의미므로 현재 글자 묶음이 하나 생겼고 알맞은 카운트에 +1
  for i in range(1, len(s)):
    if s[i - 1] != s[i]:
      if s[i] == '0':
        count_0 += 1
      else:
        count_1 += 1

  return min(count_0, count_1)

print(solution(s='0001100'))
print(solution(s='011010'))
print(solution(s='1111'))
print(solution(s='000001'))
print(solution(s='11001100110011000001'))
print(solution(s='11101101'))