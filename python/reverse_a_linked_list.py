#Reverse a Singly Linked List

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



node = head
while node != None:
  print node.data
  node = node.next
  
def reverseList(head):
  if(head.next != None):
    reverseList(head.next).next = head;
    head.next = None
  return head
  
def reverseList1(head):
  temp = None
  next = None
  while(head != None):
    next = head.next
    head.next = temp
    temp = head
    head = next
  return temp  
    
reverseList(head)

node = node9

while node != None:
  print node.data
  node = node.next
