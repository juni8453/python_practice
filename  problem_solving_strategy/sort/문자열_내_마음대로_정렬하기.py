def solution(strings, n):
    # x[n] 기준으로 정렬하고 같다면 x 기준으로 사전 정렬
    # 정렬 기준을 여러 개 사용하고 싶다면 튜플로 지정하면 됨
    answer = sorted(strings, key=lambda x: (x[n], x))

    # 미리 사전 정렬 후 x[n] 기준으로 정렬
    answer = sorted(sorted(strings), key=lambda x: x[n])

    return answer

print(solution(strings=['abce', 'abcd', 'cdx'], n=2))