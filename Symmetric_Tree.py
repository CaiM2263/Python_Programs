#A program that determines if a binary tree is symmetric
class Node:
  def __init__(self,value):
    self.left=None
    self.right=None
    self.value=value
def symmetric(root):
  if not root:
    return True
  left_list=[]
  right_list=[]
  def preorder_l(root,left_list):
    if not root:
      left_list.append('null')
    if root:
      left_list.append(root.value)
      preorder_l(root.left,left_list)
      preorder_l(root.right,left_list)
    return left_list
  
  def preorder_r(root, right_list):
    if not root:
      right_list.append('null')
    if root:
      right_list.append(root.value)
      preorder_r(root.right,right_list)
      preorder_r(root.left,right_list)
    return right_list
  preorder_l(root.left,left_list)
  preorder_r(root.right,right_list)
  return left_list==right_list

if __name__=='__main__':
  root=Node(1)
  root.left=Node(2)
  root.right=Node(2)
  root.left.left=Node(3)
  root.left.right=Node(4)
  root.right.left=Node(6)
  root.right.right=Node(3)
  print(symmetric(root))
