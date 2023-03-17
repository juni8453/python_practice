from algorithm.linked_list_practice.Node import Node

class LinkedList(object):
  def __init__(self):
    self.head = None

  def append(self, value):
    new_node = Node(value)
    # 노드가 하나도 없는 상태에서만(처음) new_node 를 가리킨다
    if self.head is None:
      self.head = new_node
    else:
      # head 부터 시작해서 마지막 노드까지 진입하고, 가장 마지막 노드가 새로 생긴 노드의 주소 값을 가질 수 있게 셋팅
      current = self.head
      while(current.next):
        current = current.next
      current.next = new_node

  def get(self, idx):
    current = self.head
    for _ in range(idx):
      current = current.next
    return current.value



ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)