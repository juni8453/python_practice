def fibo(n):
    if n == 1 or n == 2:
        return 1

    left = fibo(n - 1)
    right = fibo(n - 2)

    # 마지막 재귀 스택일 때 최초 호출 부분인 answer = fibo(n) 으로 결과 응답
    return left + right


def solution(n):
    answer = fibo(n)
    return answer


print(solution(6))