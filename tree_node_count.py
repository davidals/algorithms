#Count elements on a binary tree
from binaryNode import *

root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(9)
node5 = Node(10)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(1)

root.left = node2
root.right = node3

node2.left = node4
node4.right = node5

node3.left = node6
node3.right = node7

node6.left = node8
node6.right = node9

def count(root):
  if(root == None):
    return 0
  return 1 + count(root.left) + count(root.right)
      
print count(root)
