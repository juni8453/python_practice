# 점화식)
# find() 재귀 호출이 6번째라면 함수를 종료하고, 그게 아니라면 재귀 호출을 통해
# 계속해서 모음을 추가한다.
# 뒤로 감아서 다음 모음을 채워넣는 식이니까 DFS 함수 내에 for 문을 사용해서 합친다.

def find(data, new_str, step):
    if step == 6: # 종료조건 명시
        return

    if new_str != '': # 최초에는 비었을 테니까 공백이 안들어가도록
        data.append(new_str)

    for alp in ['A', 'E', 'I', 'O', 'U']:
        # join([a, b]) 는 a 와 b 문자열을 합친다는 뜻
        find(data, ''.join([new_str, alp]), step + 1)

def solution(word):
    data = []
    find(data, '', 0)

    return data.index(word) + 1