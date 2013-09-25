"""
Given a BST and 2 values, find their least common ancestor.
"""
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
node4.right = node5

node3.left = node6
node3.right = node7

node6.left = node8
node6.right = node9

def LCA(a,b,root):
	if(a > b):
		raise Exception("a should be less than b")
	if (root.data >= a and root.data <= b):
		return root
	if (root.data <= a and root.data <= b):
		return LCA(a, b, root.right)
	if (root.data >= a and root.data >= b):
		return LCA(a, b, root.left)
	raise Exception("Not a BST or elements are not on tree")

assert LCA(12,14,r).data == 12
assert LCA(5,11,r).data == 10
assert LCA(11,14,r).data == 12
assert LCA(12,18,r).data == 15
