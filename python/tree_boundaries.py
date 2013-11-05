#Print the boundaries of a tree
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

'''
		1
	   / \	
	 2    3
   /	 / \
  4     6   7
   \   / \
	5 8  9

'''
#We will print this tree on a Counter-clockwise fashion
def print_boundaries(node):
	print_left(node)
	print_leaves(node)
	print_right(node)

def is_leaf(node):
	return node.right == None and node.left == None
#Pre-order traversal
def print_left(node):
	if(node != None):		
		if(not is_leaf(node)):
			print node.data,
			print_left(node.left)

#In-order traversal
def print_leaves(node):
	if(node != None):
		print_leaves(node.left)
		if(is_leaf(node)):
			print node.data,
		print_leaves(node.right)


#Pos-order traversal
def print_right(node):
	if(node != None):
		if(not is_leaf(node)):
			print_right(node.right)
			if(node.right != None):
				print node.data,

print_boundaries(root)
