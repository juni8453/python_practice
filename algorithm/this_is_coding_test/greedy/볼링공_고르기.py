n, m = map(int, input().split())
data = list(map(int, input().split()))
answer = 0
ball_weight = [0] * (m + 1)

for i in data:
  ball_weight[i] += 1

# 무게가 1인 볼링공 부터 탐색
for i in range(1, ball_weight):

  # 선택한 볼링공 제외 나머지 볼링공 갯수
  # 빼주는 이유는, 무게가 i 인 경우의 수를 제외해야하기 떄문.
  n -= ball_weight[i]
  count = n * ball_weight[i] # 나머지 볼링공 갯수 * 무게가 i 인 볼링공 갯수
  answer += count

print(answer)