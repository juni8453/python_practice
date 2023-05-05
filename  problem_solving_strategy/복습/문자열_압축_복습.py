def solution(s):
    #     점화식 - s[i:i + unit]
    #     s[0:1], s[1:2], s[2:3] ...
    #     s[0:2], s[2:4], s[4:6] ...
    #     s[0:3], s[3:6], s[6:9] ...
    result = ''
    count = []

    if len(s) == 1:
        return 1

    # s 길이의 절반 이상만 탐색하면 된다. (절반 이상 넘어가면 어짜피 압축 안되니까)
    # 1부터 압축 단위(unit)를 지정해서 문자열을 압축해본다.
    for unit in range(1, (len(s) // 2) + 1):
        # print('첫 번째 for 시작')
        zip_count = 1
        slice_str = s[:unit]
        # print(result)

        # 그 다음 비교 문자열 뽑아내서 비교
        for i in range(unit, len(s) + 1, unit):
            # print('slice_str:', slice_str)
            # print('s[i:i+unit]:', s[i:i+unit])
            if slice_str == s[i:i + unit]:
                zip_count += 1
                # print('zip_count:', zip_count)

            else:
                if zip_count != 1:
                    result += (str(zip_count) + slice_str)
                else:
                    result += slice_str

                zip_count = 1
                slice_str = s[i:i+unit]
                # print('result:', result)
                # print('slice_str:', slice_str)
                # print()

        # 자르고 남는 문자열을 그대로 붙여줘야 한다.
        if s[i:i + unit] != '':
            result += s[i:i + unit]
            # print('붙일게 남았나 ?')
            # print('result:',result)

        # 한 번 비교가 끝났으면 다음 기준으로 넘어가기 전에 result 초기화
        count.append(len(result))
        result = ''
        # print('count:', count)

    answer = min(count)
    print(answer)

    return answer

# 문자열을 1개 이상의 단위로 잘라서 압축하려고 한다.
# ababcdcdababcdcd -> 1개 단위로는 못자르지만
# 2개 단위로 자르면 2ab2cd2ab2cd 로 압축할 수 있다.
# 8개 단위로 자르면 2ababcdcd 로 압축할 수 있다.
# 즉, 몇 개 이상의 단위로 자를 것인지 기준을 조정하면서 가장 짧게 압축할 수 있는 것을 찾아야 한다.
# s 길이는 10^3 이므로 O(N^2) 알고리즘으로도 충분히 풀 수 있을 듯