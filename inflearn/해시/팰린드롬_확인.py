# 1. 배열을 모두 뒤지면서 직접 원소를 바꾸는 방법은 비효율적 -> 너무 어려움
# 2. 일반화 해본 결과,
    # len(s) 가 짝수라면 모든 원소의 빈도수가 짝수여야한다.
    # len(s) 가 홀수라면 모든 원소의 빈도수는 하나의 원소를 제외한 원소의 빈도수가 짝수여야한다.

# 4. dict 을 확인하면서 빈도수가 홀수인 경우를 체크해 count 값을 증가시킨다.
# 5. count 가 1 초과라면 False, 1 이거나 0 인 경우는 True 를 반환하도록 한다.
# 즉, 모든 원소 빈도수가 짝수면 무조건 팰린드롬이 가능, 홀수 빈도수를 가지는 값이 하나 초과라면 팰린드롬이 불가능하다.

from collections import defaultdict

def solution(strings):
    strings_dict = defaultdict(int)
    for s in strings:
        strings_dict[s] += 1

    count = 0
    for value in strings_dict.values():
        if value % 2 != 0:
            count += 1

    # if count == 1 and (len(strings) % 2) != 0:
    #     return True


    return count <= 1


print(solution('abacbaa'))
print(solution('abaaceeffkckbaa'))
print(solution('abcabbcc'))
print(solution('sgsgsgabaaaecececekefefkccckbsgaaffsgsg'))
print(solution('aabcefagcefbcabbcc'))