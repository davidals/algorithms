/**
 * Created with IntelliJ IDEA.
 * User: DavidAnderson
 * Date: 11/11/13
 * Time: 21:08
 * To change this template use File | Settings | File Templates.
 */
public class RotateMatrix {

    public static void rotate90Degrees(int[][] matrix){
        int n = matrix.length;
        for(int i = 0; i < n/2; i++){
            doSwaps(matrix,i,n);
        }
    }

    private static void doSwaps(int[][] matrix, int offset, int n){
        int i = offset;
        for(int j = offset; j< n-1-offset; j++){
            swap(matrix, offset, j, j, n-1-offset);
            swap(matrix, offset, j, n-1-offset, n-1-j);
            swap(matrix, offset, j, n-1-j, offset);
        }
    }

    private static void swap(int[][] matrix, int i1, int j1, int i2, int j2) {
        int temp = matrix[i1][j1];
        matrix[i1][j1] = matrix[i2][j2];
        matrix[i2][j2] = temp;
    }
}
