#Find all ancestors of a node
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

def all_ancestors(root, key):
  if(root == None):
    return False
  if(root.data == key):
    return True
  else:
    result = all_ancestors(root.left,key) or all_ancestors(root.right,key)
  if(result):
    print root.data
  return result


all_ancestors(root,9)