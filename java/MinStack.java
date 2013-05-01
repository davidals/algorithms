//A stack that returns the minimum element in O(1) time
import java.util.Stack;

public class MinStack {

 private Stack min;
 private Stack main;
 
 public MinStack()
 {
  this.min = new Stack();
  this.main = new Stack();
 }
 
 public void push(Integer data){
  main.push(data);
  if(min.isEmpty() || data <= min.peek())
   min.push(data);
 }
 
 public Integer pop(){
  int result = main.pop();
  if(result == min.peek())
   min.pop();
  return result;
 }
 
 public Integer getMinimum(){
  return min.peek();
 }
}