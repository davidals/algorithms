import java.util.HashMap;
import java.util.HashSet;
public class MaxSubstringWithoutRepetitions {

    public static String find(String s){
        if(s.equals("")) return "";
        if(s == null) return null;
        int max = 0;
        int begin = 0;
        HashSet<Character> found = new HashSet<Character>();
        char[] chars = s.toCharArray();
        for(int i = 0; i < chars.length; i++){
            //Impossible to find a bigger substring
            if(chars.length - i < max) break;
            found.clear();
            found.add(chars[i]);
            for(int j = i+1; j <= chars.length; j++){
                if(j  == chars.length){
                    int currentRange = j-i;
                    if(currentRange > max){
                        max = currentRange;
                        begin = i;
                    }
                }
                else if(found.contains(chars[j])){
                    int currentRange = j-i;
                    if(currentRange > max){
                        max = currentRange;
                        begin = i;
                    }
                    break;
                }
                else{
                    found.add(chars[j]);
                }
            }
        }
        if(max == 1) return chars[begin] + "";
        return s.substring(begin, begin + max);
    }

    public static String find2(String s){
        if(s.equals("")) return "";
        if(s == null) return null;
        HashMap<Character, Integer> found = new HashMap<Character,Integer>();
        char[] chars = s.toCharArray();
        int[] maxSoFar = new int[chars.length];
        maxSoFar[0] = 1;
        found.put(chars[0],0);
        for(int i = 1; i < chars.length; i++){
            if(found.containsKey(chars[i])){
                maxSoFar[i] = Math.min(i - found.get(chars[i]), maxSoFar[i-1] + 1);
            }
            else{
                maxSoFar[i] = maxSoFar[i-1] + 1;
            }
            found.put(chars[i],i);
        }

        int maxIndex = maxIndex(maxSoFar);
        return s.substring(maxIndex - maxSoFar[maxIndex] + 1, maxIndex+1);
    }

    public static int maxIndex(int[] arr){
        int max = 0;
        for(int x : arr) max = x > max? x : max;
        for(int i = 0; i < arr.length; i++)
            if(arr[i] == max) return i;
        return -1;
    }
}
