/**
 * Created with IntelliJ IDEA.
 * User: DavidAnderson
 * Date: 11/11/13
 * Time: 21:27
 * To change this template use File | Settings | File Templates.
 */
public class EncodeStringWithDuplicates {
    public static String encode(String s){
        if(s == null) return null;
        char[] chars = s.toCharArray();
        char last = chars[0];
        int count = 1;
        StringBuilder builder = new StringBuilder();
        builder.append(last);
        for(int i = 1; i< chars.length; i++){
            if(!(chars[i] == last)){
                last = chars[i];
                builder.append(count);
                builder.append(last);
                count = 1;
            }
            else{
                count++;
            }

            if(i+1 == chars.length) {
                builder.append(count);
            }
        }
        return builder.toString();
    }
}
