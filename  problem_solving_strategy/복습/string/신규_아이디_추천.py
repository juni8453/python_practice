def solution(new_id):
    # 1) 대문자를 소문자로 치환한다.
    new_id = new_id.lower()

    # 2) 소문자, 숫자, -, _, . 가 아닌 모든 문자를 제거한다.
    for ch in new_id:
        if not (97 <= ord(ch) <= 122): # 소문자가 아니고,
            if not (48 <= ord(ch) <= 57): # 숫자가 아니고,
                if ch != '-' and ch != '_' and ch != '.':
                    new_id = new_id.replace(ch, '')

    # 3) '.' 이 2개 이상 연속된다면 하나로 치환한다.
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    # 4) '.' 이 [0], [-1] 에 있다면 제거한다.
    new_id = new_id.strip('.')

    # 5) 문자열 길이가 0 이라면 'a' 를 대입한다.
    if len(new_id) == 0:
        new_id = 'a'

    # 6) 문자열 길이가 16 이상이라면 앞 15 문자까지 자른다.
    if len(new_id) >= 16:
        new_id = new_id[0:15]

        if new_id[-1] == '.':
            new_id = new_id.rstrip('.')

    # 7) 문자열 길이가 2 이하라면 마지막 문자를 3이 될 때 까지 붙여준다.
    if len(new_id) < 3:
        last = new_id[-1]

        while len(new_id) < 3:
            new_id += last

    return new_id


print(solution('abcdefghijklmn.p'))
print(solution('...!@BaT#*..y.abcdefghijklm'))
print(solution('z-+.^.'))

