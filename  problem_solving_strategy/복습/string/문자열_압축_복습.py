def solution(s):
    answer = 1e15

    # 첫 번째 for 문은 자르는 크기를 정해서 기준 문자열을 만들어주는 역할
    for slice_len in range(1, len(s) // 2 + 1):
        zip_count = 1
        slice_str = s[:slice_len]
        strs = ''

        # 두 번째 for 문은 문자열 끝까지 압축 시도를 담당하는 역할
        for i in range(slice_len, len(s) + 1, slice_len):
            compare_str = s[i:i+slice_len]

            # 기준 문자열 slice_str 와 비교 문자열 compare_str 가 같다면 zip_count 를 증가
            if slice_str == compare_str:
                zip_count += 1

            # slice_str 과 compare_str 가 다르다면 answer 배열에 zip_count 와 slice_str 추가
            else:
                # 하나도 압축이 안됬다면,
                if zip_count == 1:
                    strs += slice_str
                else:
                    strs = strs + str(zip_count) + slice_str

                # 다음 비교 대비
                slice_str = compare_str
                zip_count = 1

        # 남은 문자를 붙여준다.
        if compare_str != '':
            strs += compare_str

        answer = min(answer, len(strs))

    return answer


# print(solution('aabbaccc')) # 7
# print(solution('ababcdcdababcdcd')) # 9
print(solution('abcabcdede')) # 8

