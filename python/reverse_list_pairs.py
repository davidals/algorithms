#Reverse list pairs


from linkedlist import *
import time



head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9


def rev_pairs(head):
  temp = None
  if(head!= None and head.next != None):
    next = head.next
    temp = next.next
    next.next = head
    head.next = rev_pairs(temp)
    return next
    
  return None
def PrintList( head ):
    node = head
    while node != None:
      print node.data
      node = node.next
      
      
head = rev_pairs(head)

PrintList(head)
