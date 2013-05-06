"""
Two trees are isomorphic if they have the same structure, but not necessarily the same values

   5
  / \
 1   4
    / 
   3

and
   6
  / \
 2   8
    / 
   3
Are isomorphic, but 
   5
  / \
 1   4
  \ 
   3
is not.

"""

from binaryNode import *
from collections import deque

root = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

root.left = node2
root.right = node3

node3.left = node4

root2 = Node(1)
rnode2 = Node(2)
rnode3 = Node(3)
rnode4 = Node(4)

root2.left = rnode2
root2.right = rnode3

rnode3.left = rnode4

def isomorphic_trees(root,root2):
  if((root != None and root2 == None) or (root == None and root2 != None) ):
    return False
  if(root == None and root2 == None):
    return True
  
  return isomorphic_trees(root.left, root2.left) and isomorphic_trees(root.right,root2.right)  

    
print isomorphic_trees(root, root2)

