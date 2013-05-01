#Discover if a list is palindrome

from linkedlist import *
import time
import math


head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(3)
node6 = Node(3)
node7 = Node(2)
node8 = Node(1)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8


def palindrome(head):
  ptr = head
  stack = []
  while(ptr != None):
    stack.append(ptr)
    ptr = ptr.next
    
  ptr = head
  length = len(stack)
  for i in range(int(math.ceil(length/2))):
    if(ptr.data != stack.pop().data):
      return False
    ptr = ptr.next
  return True
    
print palindrome(head)
