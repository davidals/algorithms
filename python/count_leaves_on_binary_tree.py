#Count leaves
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

def count_leaves(root):
  if(root == None):
    return
    
  queue = deque([])
  queue.append(root)
  count = 0
  while(len(queue)>0):
    node = queue.popleft()
    if(node.left != None):
      queue.append(node.left)
    if(node.right != None):
      queue.append(node.right)
    if(node.left == None and node.right == None):
      count+= 1
 
  
  return count

def count_full_nodes(root):
  if(root == None):
    return
    
  queue = deque([])
  queue.append(root)
  count = 0
  while(len(queue)>0):
    node = queue.popleft()
    if(node.left != None):
      queue.append(node.left)
    if(node.right != None):
      queue.append(node.right)
    if(node.left != None and node.right != None):
      count+= 1
 
  
  return count

print count_full_nodes(root)
