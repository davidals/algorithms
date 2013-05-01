#Print a tree upside down
from binaryNode import *

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

def print_bottom_up(root):
  if(root == None):
    return
    
  stack = []
  level = []
  level.append(root)
  stack.append(level)
  
  while(len(level)>0):
    nextLevel = []
    for node in level:
      if(node.left):
        nextLevel.append(node.left)
      if(node.right):
        nextLevel.append(node.right)
    stack.append(nextLevel)
    level = nextLevel
 
  while(len(stack)> 0):
    level = stack.pop()
    for node in level:
      print node.data, " " ,
    print ""
    
print_bottom_up(root)
