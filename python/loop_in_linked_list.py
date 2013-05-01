#Find the beginning of the loop and how much items are in the loop

from linkedlist import *

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
node9.next = node4


def print_beginning_and_count(head):

  if(head.next == None or head.next.next == None):
    print "No Loops"
    return
  slow = head.next 
  fast = head.next.next
  
  slowMoves = 1
  fastMoves = 2
  while(slow != fast):
    slow = slow.next
    fast = fast.next
    if(fast != None and fast.next != None):
      fast = fast.next
    else:
      print "No Loops"
      return
    slowMoves += 1
    fastMoves += 2
  
  print slowMoves, fastMoves
  slow = head
  
  while(slow != fast):
    slow = slow.next
    fast = fast.next
    
  print "Loop starts at " + str(slow.data)
  
  count = 0
  slow = slow.next
  while(slow != fast):
    slow = slow.next
    count += 1
  
  print "Size is " + str(count)
 
print_beginning_and_count(head)
