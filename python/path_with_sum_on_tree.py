#Find path with sum
from binaryNode import *
from collections import deque

root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)

root.left = node2
root.right = node3

node2.left = node4
node4.right = node5

node3.left = node6
node3.right = node7

node6.left = node8
node6.right = node9

def path_with_sum(root, value):
  if(root == None):
    return value == 0
  else:
    return path_with_sum(root.left, value - root.data) or path_with_sum(root.right, value - root.data)


  

print path_with_sum(root,15)
