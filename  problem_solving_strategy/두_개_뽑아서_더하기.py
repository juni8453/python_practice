from itertools import combinations

def solution(numbers):
    answer = set()
    selects = list(combinations(numbers, 2))
    for a, b in selects:
        answer.add(a + b)

    return sorted(answer)