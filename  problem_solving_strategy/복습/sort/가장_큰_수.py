from functools import cmp_to_key

def solution(numbers):
    # numbers 의 원소는 0 이상 1,000 이하
    # numbers = [0, 0, 0, 0 ,0 ....]
    if sum(numbers) == 0:
        return str(0)

    # numbers 원소를 문자열로 바꾼다.
    numbers = [str(number) for number in numbers]

    # 앞 문자와 뒷 문자를 합쳐서 비교한다.
    numbers.sort(key=cmp_to_key(lambda x, y: int(x + y) - int(y + x)), reverse=True)

    return ''.join(numbers)

print(solution([0,0,0]))
# print(solution([6, 10, 2]))
# print(solution([3, 30, 34, 5, 9]))