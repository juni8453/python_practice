import re

def solution(phone_number):
    return re.sub('\d(?=\d{4})', '*', phone_number)


print(solution('01033334444'))
print(solution('027778888'))

# 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수 작성