#Find the nth node from tail
from linkedlist import *

def nth_node_from_tail(head, n):
  nth = head
  current = head
  for i in range(n):
    current = current.next
  while(current.next):
    current = current.next
    nth = nth.next
  return nth
  
  
List = LinkedList()
List.AddNode(1)
List.AddNode(2)
List.AddNode(3)
List.AddNode(4)
List.AddNode(5)
List.AddNode(6)
List.AddNode(7)


print nth_node_from_tail(List.head, 3).data
