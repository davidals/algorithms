import java.util.HashMap;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;

/**
 * Created with IntelliJ IDEA.
 * User: DavidAnderson
 * Date: 08/11/13
 * Time: 21:16
 * To change this template use File | Settings | File Templates.
 */
public class IsomorphicStrings {

    private static class Mapping{

        private final Character c;
        private final List<Integer> integers;

        public Mapping(Character c, List<Integer> integers) {
            this.c = c;
            this.integers = integers;
        }

        private Character getC() {
            return c;
        }

        private List<Integer> getIntegers() {
            return integers;
        }
    }

    public static List<Mapping> getMap(String s) throws Exception {
        if(s== null || s.isEmpty()) throw new Exception("String cannot be null or empty");
        LinkedHashMap<Character, List<Integer>> map = new LinkedHashMap<Character, List<Integer>>();
        char[] chars = s.toCharArray();
        for(int i = 0; i < chars.length; i++){
            if(!map.containsKey(chars[i])) map.put(chars[i], new ArrayList<Integer>());
            map.get(chars[i]).add(i);
        }
        List<Mapping> result = new ArrayList<Mapping>();
        for(Character c : map.keySet())
            result.add(new Mapping(c, map.get(c)));
        return result;
    }

    public static boolean areIsomorphic(String a, String b) throws Exception {
        if(a.length() != b.length()) return false;
        List<Mapping>  mapA = getMap(a);
        List<Mapping>  mapB = getMap(b);
        if(mapA.size() != mapB.size()) return false;
        for(int i = 0; i< mapA.size(); i++){
            Mapping fromA = mapA.get(i);
            Mapping fromB = mapB.get(i);
            if(fromA.getIntegers().size() != fromB.getIntegers().size()) return false;
            for(int j = 0; j < fromA.getIntegers().size(); j++)
                if(fromA.getIntegers().get(j) != fromB.getIntegers().get(j)) return false;
        }
        return true;
    }
}
