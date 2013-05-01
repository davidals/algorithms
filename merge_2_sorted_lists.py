#Merge 2 sorted linked lists

from linkedlist import *

head1 = Node(1)
node2 = Node(3)
node3 = Node(5)
node4 = Node(7)

head2 = Node(2)
node6 = Node(4)
node7 = Node(6)
node8 = Node(8)


head1.next = node2
node2.next = node3
node3.next = node4

head2.next = node6
node6.next = node7
node7.next = node8


def merge(head1, head2):
  res = []
  ptr1 = head1
  ptr2 = head2
  
  while(ptr1 != None or ptr2 != None):
    if (ptr1 == None):
      res.append(ptr2)
      ptr2 = ptr2.next
    elif (ptr2 == None):
      res.append(ptr1)
      ptr1 = ptr1.next      
    elif(ptr1.data<ptr2.data):
      res.append(ptr1)
      ptr1 = ptr1.next
    else:
      res.append(ptr2)
      ptr2 = ptr2.next
  print [x.data for x in res]
  
merge(head1, head2)    

