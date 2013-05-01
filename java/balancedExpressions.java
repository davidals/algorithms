public class ExpressionChecker {

 private static Character[] openingDelimiters = {'(','{','['};
 private static Character[] closingDelimiters = {')','}',']'};
 
 public boolean isBalanced(String expr) throws Exception{
  if(expr == null || expr.isEmpty())
   throw new Exception("Null or empty parameter");
   
  Stack stack = new Stack();
  for(int i = 0; i < expr.length(); i++){
   Character c = expr.charAt(i);
   if(isClosingDelimiter(c)){
    Character pop = stack.pop();
    while(!isOpeningDelimiter(pop))
     pop = stack.pop();
    if(!isPair(pop,c))
     return false;
   }
   else
    stack.push(c);
  }
  while(!stack.isEmpty()){
   Character pop = stack.pop();
   if(isOpeningDelimiter(pop) || isClosingDelimiter(pop) )
    return false;
  }
   
  return true;
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

}



public class ExpressionCheckerTest {

 ExpressionChecker target = new ExpressionChecker();
 
 @Test
 public void test1() throws Exception {
  String expr = "(A+B)+(C+D)";
  assertTrue(target.isBalanced(expr));
 }
 
 @Test
 public void test2() throws Exception {
  String expr = "((A+B)+(C+D)";
  assertFalse(target.isBalanced(expr));
 }
 
 @Test
 public void test3() throws Exception {
  String expr = "((A+B)+(C+D))";
  assertTrue(target.isBalanced(expr));
 }
 
 @Test
 public void test4() throws Exception {
  String expr = "((A+B)+[C+D]}";
  assertFalse(target.isBalanced(expr));
 }
 

 @Test
 public void test5() throws Exception {
  String expr = "A+ {(A+B)+[C+D]}";
  assertTrue(target.isBalanced(expr));
 }

}