#Zig zag traversal on a tree
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
node2.right = node5

node3.left = node6
node3.right = node7


def print_level(level,reverse):
    if(reverse):
        for node in reversed(level):
            print node.data,
    else: 
        for node in level:
            print node.data,
    print '\n'

def zig_zag_traversal(root):
  level = []
  next_level = []
  level.append(root)
  left_to_right = True;
  while(len(level) > 0):
        print_level(level,not left_to_right)

        left_to_right = not left_to_right


        for node in level:
            if(node.left != None):
                next_level.append(node.left)
            if(node.right != None):
                next_level.append(node.right)
           
        level = next_level
        next_level = []



zig_zag_traversal(root)