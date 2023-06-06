from itertools import permutations

def checkPrime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def solution(numbers):
    answer = []
    num_list = list(numbers)
    per_list = []

    # permutations 활용해서 num_list 조합을 만들고,
    for i in range(1, len(num_list) + 1):
        per_list.append(list(permutations(num_list, i)))

    # 숫자로 변환한다.
    new_nums = []
    for i in per_list:
        for j in i:
            new_nums.append(int(''.join(j)))

    # 해당 조합이 소수인지 판단한다.
    # [1, 7, 17, 71]
    for num in new_nums:
        if checkPrime(num):
            answer.append(num)

    # 중복을 제거한 뒤 반환한다.
    return len(set(answer))

print(solution("17"))
print(solution("011"))