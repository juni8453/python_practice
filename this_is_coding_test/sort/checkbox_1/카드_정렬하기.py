import heapq

heap = []
n = int(input())
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

answer = 0

while len(heap) != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    sum = a + b
    answer += sum
    heapq.heappush(heap, sum)

print(answer)
