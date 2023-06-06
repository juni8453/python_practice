def radixChange(num, radix):
    if num == 0:
        return '0'

    nums = []
    while num:
        num, digit = divmod(num, radix)
        nums.append(str(digit))

    return ''.join(reversed(nums))

def solution(n):
    return int(radixChange(n, 3)[::-1], 3) # 3진수를 거꾸로 돌린 해당 배열을 다시 10진수로 변환

print(solution(45))