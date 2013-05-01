#Given inorder and preorder traversal, rebuild tree

class TreeConstructor:
  def __init__(self):
    self.preIndex = 0

  def rebuild_tree(self,inorder, preorder):
    
    if(len(inorder) == 0):
      return None

    data = preorder[self.preIndex]
    newNode = Node(data)
    self.preIndex +=1
    inIndex = search(data,inorder)
    
    if(inIndex == -1):
      raise Exception("Traversals don't match")

    newNode.left = self.rebuild_tree(inorder[:inIndex],preorder)
    newNode.right = self.rebuild_tree(inorder[inIndex+1:], preorder)
    return newNode