# 진법 변환기
def radixChange(num, radix):
    if num == 0:
        return 0

    nums = []
    while num:
        num, digit = divmod(num, radix)
        nums.append(str(digit))

    return ''.join(reversed(nums))

def solution(n):
    # 1. n 을 3진법으로 변환하고 반대로 뒤집는다.
    changed_n_by3 = radixChange(n, 3)[::-1]

    # # 2. x 진수 -> 10 진수는 간단하게 int(<진법이 있는 문자열>, <해당 문자열의 진법>)
    return int(changed_n_by3, 3)


print(solution(45))
print(solution(125))