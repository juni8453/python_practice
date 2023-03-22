from sys import stdin

n = int(input())
tree = dict()

for i in range(n):
  node, left, right = stdin.readline().split()
  tree[node] = [left, right] # root 를 key, left 는 [0] right[1] 에 저장

# 전위 순회
def preorder(root):
  if root != '.':
    print(root, end='')
    preorder(tree[root][0])
    preorder(tree[root][1])

# 중위 순회
def inorder(root):
  if root != '.':
    inorder(tree[root][0])
    print(root, end='')
    inorder(tree[root][1])

# 후위 순회
def postorder(root):
  if root != '.':
    postorder(tree[root][0])
    postorder(tree[root][1])
    print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')