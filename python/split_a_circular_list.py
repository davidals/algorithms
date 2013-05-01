#Split a circular list in half

from linkedlist import *
import time
import math


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
node9.next = head

def split(head):
  ptr1 = head
  ptr2 = head.next
  count = 1
  while(ptr1!= ptr2):
    count += 1
    ptr2 = ptr2.next
  
  for i in range(int(math.ceil(count/2))):
    print ptr1.data
    ptr1 = ptr1.next
    
  list2 = ptr1.next
  ptr2 = list2
  ptr1.next = head
  
  while(list2.next != head):
    list2 = list2.next
    
  list2.next = ptr2
  PrintList(head)
  
def PrintList( head ):
    node = head
    while node != None:
      time.sleep(1)      
      print node.data
      node = node.next
  
split(head)  


