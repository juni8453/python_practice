def solution(records):
  answer = []
  dict_nickname = dict()

  for record in records:
    record_split = record.split()
    keyword = record_split[0]
    uid = record_split[1]

    if keyword != 'Leave':
      nickname = record_split[2]

    if keyword == 'Leave':
      answer.append(uid + '님이 나갔습니다.')

    if keyword == 'Enter':
      dict_nickname[uid] = nickname
      answer.append(uid + '님이 들어왔습니다.')

    if keyword == 'Change':
      dict_nickname[uid] = nickname

  for i in range(len(answer)):
    uid, text = answer[i].split('님')
    new__nickname = dict_nickname[uid]
    answer[i] = new__nickname + '님' + text

  return answer

print(solution(records=[
  "Enter uid1234 Muzi",
  "Enter uid4567 Prodo",
  "Leave uid1234",
  "Enter uid1234 Prodo",
  "Change uid4567 Ryan"]))