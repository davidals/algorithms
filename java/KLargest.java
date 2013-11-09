/**
 * Created with IntelliJ IDEA.
 * User: DavidAnderson
 * Date: 08/11/13
 * Time: 20:40
 * To change this template use File | Settings | File Templates.
 */
public class KLargest {

    public static int[] kLargest(int[] arr, int k, int begin, int end) throws Exception {
        if(k > arr.length) throw new Exception("K should be less than the array size");
        if(k == 0) throw new Exception("K should be greater than zero");
        if(begin <0 || end > arr.length) throw new Exception("Begin and end should be within the array");
        if(end < begin) throw new Exception("Begin should be less than end");

        int partitionElement = arr[begin];
        int n = arr.length;
        int i = begin;
        int j = end - 1;
        while(i < j){
            while(arr[i] < partitionElement){
                i++;
                if(i>j || i > end)
                    break;
            }
            while(arr[j] >= partitionElement){
                j--;
                if(i >= j || j < 0)
                    break;
            }
            swap(arr,i,j);
        }
        swap(arr, j, begin);
        if(n-j == k){
            int[] result = new int[k];
            for(i = 0; i< result.length; i++)
                result[i] = arr[j++];
            return result;
        }
        if(n-j>k) return kLargest(arr,k, j+1, end);
        return kLargest(arr,k,begin,j);
    }

    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
