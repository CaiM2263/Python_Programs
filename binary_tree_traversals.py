class Node:
  def __init__(self,value):
    self.left=None
    self.right=None
    self.value=value

def preorder(root):
  if root:
      print(root.value, end=' ')
      preorder(root.left)
      preorder(root.right)

def inorder(root):
  if root:
    inorder(root.left)
    print(root.value, end=' ')
    inorder(root.right)

def postorder(root):
  if root:
    postorder(root.left)
    postorder(root.right)
    print(root.value, end=' ')

def levelorder(root):
  result = []
  if not root:
      return result
  queue = deque([root])
  while queue:
      level_values = []
      level_size = len(queue)
      for _ in range(level_size):
          node = queue.popleft()
          level_values.append(node.value)
          if node.left:
              queue.append(node.left)
          if node.right:
              queue.append(node.right)
      print(level_values)
  return result

def maxDepth(root):
  if root is None:
      return 0
  else:
      lDepth = maxDepth(root.left)
      rDepth = maxDepth(root.right)
      if (lDepth > rDepth):
          return lDepth+1
      else:
          return rDepth+1
        
def balance(root):
      if root is None:  
          return 0
      lDepth =balance(root.left)
      rDepth=balance(root.right)
      if lDepth < 0 or rDepth < 0 or abs(lDepth - rDepth) > 1:
          return -1
      return max(lDepth, rDepth) + 1
  


if __name__=='__main__':
  root=Node(1)
  root.left=Node(2)
  root.right=Node(3)
  root.left.left=Node(4)
  root.left.right=Node(5)
  root.right.left=Node(6)
  root.right.right=Node(7)
  root.right.right.left=Node(8)
  print('Depth First Search/Preorder Traversal')
  preorder(root)
  print('\n\n')
  print('Inorder Traversal')
  inorder(root)
  print('\n\n')
  print('Postorder Traversal')
  postorder(root)
  print('\n\n')
  print('Level Order Traversal')
  levelorder(root)
  print('\n\n')
  print('Max Depth of Binary Tree')
  print(maxDepth(root))
  print('\n\n')
  print('Balanced Binary Tree')
  print(balance(root)>=0)
  
