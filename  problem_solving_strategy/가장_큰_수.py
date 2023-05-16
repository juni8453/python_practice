# 첫 번재 풀이

from functools import cmp_to_key

def solution(numbers):
    # numbers = [0, 0, 0 ...] 인 경우 예외처리
    if sum(numbers) == 0:
        return '0'

    # 문자열 리스트로 바꾼다.
    numbers = [str(i) for i in numbers]
    numbers.sort(key=cmp_to_key(
        lambda x, y: int(x + y) - int(y + x)), reverse=True)

    return ''.join(numbers)

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([4, 35]))


# 합쳤을 때 가장 큰 수를 문자열로 반환하는 함수 solution() 작성
# 단순히 내림차순 했을 때 3, 30, 34 라는 예외가 있기 때문에 복합적으로 정렬을 거친 뒤 내림차순을 적용해야하는 문제
# ['3', '30', '34'] 라고 했을 때 만들 수 있는 가장 큰 수는 '34330' 즉, '3' > '34' 라는 뜻
# 즉, '3' + '30' = '330' 인 경우, '30' + '3' = '303' 인 경우를 비교해서 0보다 작으면 위치를 바꾸도록 복합 정렬 조건 설정


# 두 번째 풀이

from functools import cmp_to_key

def solution(numbers):
    if sum(numbers) == 0:
        return '0'

    numbers = [str(i) for i in numbers]
    numbers.sort(key=lambda x: x*4, reverse=True)

    return ''.join(numbers)

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([4, 35]))

# 첫 번째 풀이는 cmp_to_key() 함수를 통해 직접적으로 정렬 함수를 만들어 사용했기 때문에 추가적인 시간 비용이 발생
# 따라서 두 번째 풀이는 cmp_to_key() 함수를 사용하지 않고 풀이
# numbers 리스트를 문자열 리스트로 변환하는 것 까지 동일
# ['1', '1000'] 이라고 한다면 만들 수 있는 가장 큰 수는 '11000' 즉, '1' > '1000' 라는 뜻
# 여기서 아이디어는 비교하려는 원소를 4번씩 곱한 뒤 문자열 아스키 코드를 앞에서부터 비교하면서 내림차순을 진행하는 것
# 4번을 곱하는 이유는 문자열 리스트의 원소 최대 값이 1,000 이라고 했기 때문에 최소 한 자리 숫자를 4자리로 늘려서 비교할 수 있도록 하기 위함
# 즉, 위의 예시로 들자면 '1111' 과 '1000100010001000' 을 비교하는 것 -> '1' 이 같으므로 '1' 과 '0' 을 비교할 것이고 '1' 이 '1000' 보다 더 큰 결론이 나옴