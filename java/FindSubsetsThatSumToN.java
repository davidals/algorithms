import java.util.LinkedList;
import java.util.List;

/**
 * Created with IntelliJ IDEA.
 * User: DavidAnderson
 * Date: 10/11/13
 * Time: 22:23
 * To change this template use File | Settings | File Templates.
 */
public class FindSubsetsThatSumToN {
    public static List<List<Integer>> findSubsetsThatSumToN(int[] arr, int n){
        List<List<Integer>> result = new LinkedList<List<Integer>>();
        for(int i = 0; i < arr.length; i++){
            for(List<Integer> l : findSubsetsThatSumToN(arr, i, n))
                result.add(l);
        }
        return result;
    }
    public static List<List<Integer>> findSubsetsThatSumToN(int[] arr, int begin, int n){
        List<List<Integer>> result = new LinkedList<List<Integer>>();
        if(n < arr[begin]) return result;
        if(arr[begin] == n){
            List<Integer> oneElement = new LinkedList<Integer>();
            oneElement.add(arr[begin]);
            result.add(oneElement);
            return result;
        }
        else{
            for(int i = 0; i< arr.length; i++){
                List<List<Integer>> childSubsets = findSubsetsThatSumToN(arr, i, n - arr[begin]);
                for(List l : childSubsets){
                    if(!l.isEmpty()){
                        l.add(arr[begin]);
                        result.add(l);
                    }
                }
            }
            return result;
        }
    }
}
