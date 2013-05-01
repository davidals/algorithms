//A linked list with amortized O(1) insertion and retrieval 
public class LinkedList {
 private class Node{
  
  private Integer value;
  private Node next;
  
  public Node(Integer value){
   this.setValue(value);    
  }
  public Integer getValue() {
   return value;
  }
  public void setValue(Integer value) {
   this.value = value;
  }
  public Node getNext() {
   return next;
  }
  public void setNext(Node next) {
   this.next = next;
  }
  
  @Override
  public String toString() {
   return value.toString();
  }
 }
 private final double reduceFactor = 2.0/3.0;
 
 private Node head;
 private Node tail;
 private Node[] array;
 private int count = 0;
 private int arraySize;
 
 public LinkedList() {
  arraySize = 10;
  this.setArray(new Node[arraySize]);
 }
 
 public void add(Integer data){
  Node newNode = new Node(data);
  if(head == null)
   head = newNode;
  if(tail != null)
   tail.setNext(newNode);
  tail = newNode;
  
  addToArray(newNode);
 }
 
 
 private void addToArray(Node newNode) {
  if(count == arraySize)
   incrementArray();
  getArray()[count++] = newNode;
 }

 private void incrementArray() {
  arraySize *= 2; 
  Node[] tempArray = new Node[arraySize];
  for (int i = 0; i < getArray().length; i++) {
   Node n = getArray()[i];
   tempArray[i] = n;
  }
  setArray(tempArray);
 }
 
 public void remove(int index){
  Node node = head;
  for(int i = 0; i < index-1; i++){
   node = node.getNext();
  }
  Node toBeRemoved = node.getNext();
  node.setNext(toBeRemoved.getNext());
  if(tail == toBeRemoved)
   tail = node;
  if(head == toBeRemoved){
   head = null;
   tail = null;
  }
  removeFromArray(index);
 }

 private void removeFromArray(int index) {
  for(int i = index; i < count; i++){
   getArray()[i] = getArray()[i+1];
  }
  count--;
  if(count < arraySize / 2)
   reduceArray();
 }

 private void reduceArray() {
  
  arraySize = (int) Math.ceil(reduceFactor* arraySize);
  Node[] tempArray = new Node[arraySize];
  for(int i = 0; i< arraySize; i++)
   tempArray[i] = getArray()[i];
  setArray(tempArray);
 }
}