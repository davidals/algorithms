"""
Given a tree, find out if it is a BST or not.
"""

import sys

class Node:

  def __init__( self, data ):
    self.data = data
    self.left = None
    self.right = None
       
    
r = Node(10)
node2 = Node(5)
node3 = Node(15)
node4 = Node(3)
node5 = Node(1)
node6 = Node(12)
node7 = Node(18)
node8 = Node(11)
node9 = Node(14)

r.left = node2
r.right = node3

node2.left = node4
node4.left = node5

node3.left = node6
node3.right = node7

node6.left = node8
node6.right = node9

def maxInt():
	return sys.maxint
def minInt():
	return	-sys.maxint - 1 

def findMax(r):
	if(r == None):
		return minInt()
	maxLeft = findMax(r.left)
	maxRight = findMax(r.right)
	return max([r.data, maxLeft, maxRight])
def findMin(r):
	if(r == None):
		return maxInt()
	minLeft = findMin(r.left)
	minRight = findMin(r.right)
	return min([r.data, minLeft, minRight])

def isBST(r):
	#Inefficient
	if(r == None):
		return True
	#print r.data, findMax(r.left), findMin(r.right)
	#print r.data, (findMax(r.left) < r.data) , (findMin(r.right) > r.data) 
	return  (
		    (findMax(r.left) < r.data) 	and
			(findMin(r.right) > r.data) and
			isBST(r.left) 				and
			isBST(r.right)
			)

def isBST2(r,prev):
	if(r == None):
		return True	
	if(r.data < prev[0]):
		print 1
		return False
	if( not isBST2(r.left,prev)):
		print 2
		return False
	prev[0] = r
	return isBST2(r.right,prev)

assert isBST(r)
assert isBST2(r, [minInt()])

