def solution(new_id):
    # 1단계) 모든 대문자를 소문자로 치환한다.
    new_id = new_id.lower()

    filtered = []
    # 2단계) 소문자, 숫자, 빼기, 밑줄, 마침표 제외 모든 문자를 제거한다.
    for s in new_id:
        if s.islower() or s.isdigit() or s == '-' or s == '_' or s == '.':
            filtered.append(s)

        new_id = ''.join(filtered)

    # 3단계) 마침표가 2번 이상 연속된 부분을 하나의 마침표로 치환한다.
    # .... 라면 .. 로 바뀌고 다시 . 로 바뀔 수 있도록
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    # 4단계) 마침표가 처음이나 끝에 위치한다면 제거한다.
    new_id = new_id.strip('.')

    # 5단계) 빈 문자열이라면 a 를 대입한다.
    if len(new_id) == 0:
        new_id = 'a'

    # 6단계) 길이가 16자 이상이면 첫 15개 문자를 제외한 나머지 문자 모두 제거
    if len(new_id) >= 16:
        new_id = new_id[:15]

    # 제거 후 마침표가 new_id 끝에 위치한다면 끝 마침표를 제거한다.
    # str[:-1] -> 맨 오른쪽 값 제외하고 모두
    if new_id[-1] == '.':
        new_id = new_id[:-1]

    # 7단계) 길이가 2자 이하라면 마지막 문자를 길이 3이 될 때까지 반복해서 끝에 붙인다.
    if len(new_id) <= 2:
        add_str = new_id[-1]

        while len(new_id) != 3:
            new_id += add_str

    return new_id

print(solution(new_id='...!@BaT#*..y.abcdefghijklm'))