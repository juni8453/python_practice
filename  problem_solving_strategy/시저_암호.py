def solution(s, n):
    my_list = []

    for i in s:

        # 공백이라면,
        if ord(i) == 32:
            my_list.append(' ')
            continue

        check_ascci = ord(i) + n

        # 대문자
        if i.isupper():
            if check_ascci <= 90: # 'Z' 범위 안이라면,
                my_list.append(chr(check_ascci))

            else: # 범위를 벗어나면 - 26
                my_list.append(chr(check_ascci - 26))

        # 소문자
        elif i.islower():
            if check_ascci <= 122: # 'z' 범위 안이라면,
                my_list.append(chr(check_ascci))

            else:
                my_list.append(chr(check_ascci - 26))

    return ''.join(my_list)