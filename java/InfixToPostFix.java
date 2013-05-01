//Convert a Infix expression to PostFix
public class InfixToPostFix {

 private static Character[] openingDelimiters = {'(','{','['};
 private static Character[] closingDelimiters = {')','}',']'};
 private static Character[] operators = {'+','-','*','/'};
 
 public String infixToPostfix(String expr) throws Exception{
  if(expr == null || expr.isEmpty())
   throw new Exception("Null or empty parameter");
  
  StringBuilder result = new StringBuilder(); 
  
  Stack stack = new Stack();
  for(int i = 0; i < expr.length(); i++){
   Character c = expr.charAt(i);
   //Case 1
   if(isOperand(c)){
    result.append(c);
   }
   //Case 2
   else if(isClosingDelimiter(c)){
    printUntilFindOpeningDelimiter(result, stack, c);
   }
   //Case 3
   else{
    printUntilFindLowerPriority(result, stack);
    stack.push(c);
   }
  }
  //Case 4
  printRemainingOperators(result, stack);
  
  return result.toString();
  
 }

 public void printUntilFindOpeningDelimiter(StringBuilder result,
   Stack stack, Character c) throws Exception {
  Character pop = null;
  do{
   if(isOpeningDelimiter(stack.peek())) 
    if(isPair(stack.peek(),c)){
     stack.pop();
     break;
    }
    else
     throw new Exception("Invalid Expression");
   
   pop = stack.pop();
   result.append(pop);
  }
  while(!isOpeningDelimiter(pop));
 }
 
 public void printUntilFindLowerPriority(StringBuilder result,
   Stack stack) {
  Character pop = null;
  if(!stack.isEmpty()) 
   do{
    if(isOpeningDelimiter(stack.peek())) break;
    pop = stack.pop();
    result.append(pop);
   }
   while(pop!= null &&  !stack.isEmpty() && !isOperand(pop) );
 }
 
 public void printRemainingOperators(StringBuilder result,
   Stack stack) {
  if(!stack.isEmpty())
   do{
    Character pop = stack.pop();
    result.append(pop);
   }while(!stack.isEmpty());
 }
 
 private boolean isOperand(Character c) {
  return !isDelimiter(c) && !isOperator(c);
 }
 
 private boolean isDelimiter(Character c){
  return isOpeningDelimiter(c) || isClosingDelimiter(c);
 }

 private boolean isPair(Character open, Character close) {
  switch(open){
  case '(' :
   return close.equals(')');
   
  case '{' :
   return close.equals('}');
  
  case '[' :
   return close.equals(']');
  }
  
  return false;
 }



 private boolean isOpeningDelimiter(Character c) {
  for(Character d : openingDelimiters)
   if(c.equals(d))
    return true;
  return false;
 }
 
 private boolean isClosingDelimiter(Character c) {
  ;
  for(Character d : closingDelimiters)
   if(c.equals(d))
    return true;
  return false;
 }
 
 private boolean isOperator(Character c){
  for(Character d : operators)
   if(c.equals(d))
    return true;
  return false;
 }

}