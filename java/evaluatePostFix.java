public int evaluatePostFix(String expr) throws Exception{
  if(expr == null || expr.isEmpty())
   throw new Exception("Null or empty parameter");
  
  Stack operands = new Stack();
  
  for(int i = 0; i < expr.length(); i++){
   Character c = expr.charAt(i);
   if(isOperand(c))
    operands.push(Integer.parseInt(c.toString()));
   else{
    if(operands.size() < 2)
     throw new Exception("Invalid expression");
    
    Integer op2 = operands.pop();
    Integer op1 = operands.pop();
    if(c.equals('+'))
     operands.push(op1 + op2);
    else if(c.equals('-'))
     operands.push(op1 - op2);
    else if(c.equals('*'))
     operands.push(op1 * op2);
    else if(c.equals('/'))
     operands.push(op1 / op2);
    else
     throw new Exception("Invalid expression");
   }
  }
  
  return operands.pop();  
 }