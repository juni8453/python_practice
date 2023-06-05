def solution(strings, n):
    # 각 단어의 인덱스 n 번째 글자를 기준으로 오름차순 정렬

    # 첫 번째 방법) 미리 정렬 후 x[n] 기준으로 정렬
    # answer = sorted(sorted(strings), key=lambda x: x[n])

    # 두 번째 방법) tuple 을 사용해 한번에 정렬
    return sorted(strings, key=lambda x: (x[n], x))


print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))