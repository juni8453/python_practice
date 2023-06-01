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
    number_list = []

    for length in range(1, len(numbers) + 1):
        number_list.append(list(permutations(numbers, length)))

    # 배열 압축
    number_list = [int(''.join(y)) for x in number_list for y in x]

    for number in number_list:
        if checkPrime(number):
            answer.append(number)

    return len(set(answer))


print(solution("17"))
print(solution("011"))
