#Check if two trees are equal
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

root2 = Node(1)
rnode2 = Node(2)
rnode3 = Node(3)
rnode4 = Node(4)
rnode5 = Node(5)
rnode6 = Node(6)
rnode7 = Node(7)
rnode8 = Node(8)
rnode9 = Node(9)

root2.left = rnode2
root2.right = rnode3

rnode2.left = rnode4
rnode4.right = rnode5

rnode3.left = rnode6
rnode3.right = rnode7

rnode6.left = rnode8
rnode6.right = rnode8

def equal_trees(root,root2):
  if(root == None and root2 == None):
    return True
  if(root == None and root2 != None):
    return False
  if(root!= None and root2 == None):
    return False
  return root.data == root2.data and equal_trees(root.left, root2.left) and equal_trees(root.right,root2.right)  

    
print equal_trees(root, root2)
