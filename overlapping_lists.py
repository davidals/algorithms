#Find the meeting point of 2 linked lists
from linkedlist import *
import time

def binary_search(a,b):
  pass

head1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)

head1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9

head2 = Node("a")
nodeB = Node("b")
nodeC = Node("c")

head2.next = nodeB
nodeB.next = nodeC
nodeC.next = node5

def find_meeting_point_quadratic(head1, head2):
  ptr1 = head1
  while(ptr1!= None):
    ptr2 = head2
    while(ptr2!= None):
      if(ptr2 == ptr1):
        return ptr2
      ptr2 = ptr2.next
    ptr1 = ptr1.next
    
  
def find_meeting_point2(head1, head2):
  ids = []
  ptr1 = head1
  while(ptr1!= None):
    ids.append(id(ptr1))
    ptr1 = ptr1.next

  ids.sort()
  ptr2 = head2
  
  while(ptr2!= None):
    if(binary_search(id(ptr2),ids)):
      return ptr2
    ptr2 = ptr2.next
      
def find_meeting_point_stacks(head1, head2):
  stack1 = []
  ptr1 = head1
  while(ptr1!= None):
    stack1.append(ptr1)
    ptr1 = ptr1.next

  stack2 = []
  ptr2 = head2
  while(ptr2!= None):
    stack2.append(ptr2)
    ptr2 = ptr2.next
    
  ptr1 = stack1.pop()
  ptr2 = stack2.pop()
  meeting = ptr1
  while(ptr1 == ptr2):
    meeting = ptr1
    ptr1 = stack1.pop()
    ptr2 = stack2.pop()
  return meeting

def find_meeting_point_map(head1, head2):
  ids = {}
  ptr1 = head1
  while(ptr1!= None):
    ids[id(ptr1)] = ptr1
    ptr1 = ptr1.next

  ptr2 = head2
  while(ptr2!= None):
    if(ids.setdefault(id(ptr2)) != None):
      return ptr2
    ptr2 = ptr2.next
           
print find_meeting_point_map(head1,head2).data

