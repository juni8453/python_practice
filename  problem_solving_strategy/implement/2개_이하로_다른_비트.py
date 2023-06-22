def find_index(my_list, element):
    try:
        index = my_list.index(element)
        return index

    except ValueError:
        return -1


def solution(numbers):
    answer = []

    # 짝수인 경우 가장 뒤 비트를 1로 변환 -> number + 1 반환하면 끝
    # 홀수인 경우 오른쪽에서 왼쪽으로 세면서 가장 먼저 '0' 이 나오는 자리와 오른쪽 자리를 교환
        # 홀수인 경우 오른쪽에서 가장 먼저 발견되는 '0' 은 바로 다음 오른쪽 자리에 '1' 이 무조건 존재
    for number in numbers:
        # 짝수인 경우,
        if number % 2 == 0:
            answer.append(number + 1)

        # 홀수인 경우
        elif number % 2 != 0:
            # 2진수로 변환 후 오른쪽 -> 왼쪽으로 탐색할 수 있도록 리스트 뒤집기
            bin_number = list(bin(number)[2:])
            bin_number.reverse()

            # 0 이 없는 2진수의 경우 맨 오른쪽에 '0' 추가 (뒤집었으니까)
            if find_index(bin_number, '0') == -1:
                bin_number.append('0')
                print(bin_number)

            # 뒤집어놨으니 앞에서부터 '0' 위치를 찾는다. 발견하면 바로 왼쪽의 1과 교환
            for bin_n in bin_number:
                if bin_n == '0':
                    first_zero_index = bin_number.index(bin_n)
                    bin_number[first_zero_index] = '1'
                    bin_number[first_zero_index - 1] = '0'
                    break

            bin_number.reverse()
            answer.append(int(''.join(bin_number), 2))

    return answer


print(solution([2, 11, 7]))

# first_zero_index = bin_number.rfind('0')
# bin_number[first_zero_index] = '1'
# bin_number[first_zero_index + 1] = '0'