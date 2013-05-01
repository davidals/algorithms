#Josephus Problem http://en.wikipedia.org/wiki/Josephus_problem


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

def findSurvivor(beginning, steps):
  ptr1 = beginning.next
  count = 1
  while(ptr1!= beginning):
    ptr1 = ptr1.next
    count += 1
  ptr1 = beginning
  ptr2 = ptr1
  for i in range(count -1):
    for i in range(steps-1):
      ptr1 = ptr1.next
    ptr2 = ptr1.next
    ptr1.next = ptr2.next
 
  return ptr1
 
findSurvivor(head,3)
      
