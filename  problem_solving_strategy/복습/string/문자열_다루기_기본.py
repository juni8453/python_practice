import re

# 정규 표현식 사용 예 1)
def solution(s):
    return bool(re.match('^(\d{4}|\d{6})$', s))


# 정규 표현식 사용 예 2)
def solution(s):
    return len(s) in [4, 6] and bool(re.match('^[0-9]*$', s))


print(solution('a123'))
print(solution('a1234'))
print(solution('1234'))
print(solution('12a4'))