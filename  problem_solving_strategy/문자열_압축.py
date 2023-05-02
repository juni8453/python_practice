def solution(s):
    answer = len(s) # 초기 값 (압축한 값의 길이와 비교할 수 있도록)

    for unit in range(1, len(s) // 2 + 1):
        res = ''
        zip_count = 1 # 현재 단위로 얼마나 압축됬는지 ?
        slice_str = s[:unit]

        for i in range(unit, len(s) + 1, unit): # 단위가 증가할 수록 반복 횟수는 줄어야 한다.
            if slice_str == s[i:i+unit]: # 압축할 수 있다면 압축 카운트 증가
                zip_count += 1

            else:
                if zip_count == 1: # 만약 하나도 압축이 안됬다면
                    res += slice_str
                else:
                    res = res + str(zip_count) + slice_str

                # 다음 for 문 대비
                slice_str = s[i:i+unit]
                zip_count = 1

        answer = min(answer, len(res))

    return answer

print(solution(s="aabbaccc"))
