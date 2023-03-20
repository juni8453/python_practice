from collections import deque

# Double Linked List 로 구현됨
# 따라서 데이터 삽입, 제거 시 O(n) 이 아닌 O(1)
queue = deque()

# enqueue() O(1)
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

# dequeue() O(1)
queue.popleft()
queue.popleft()
queue.popleft()

