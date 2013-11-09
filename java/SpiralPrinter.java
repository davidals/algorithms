public class SpiralPrinter {

    public static void print(int[][] matrix){
        int lowerI = 0;
        int upperI = matrix.length - 1;
        int lowerJ = 0;
        int upperJ = matrix[0].length - 1;

        while(true){
            if(canContinue(lowerI, upperI, lowerJ, upperJ)){
                for (int j = lowerJ; j <= upperJ; j++)
                    System.out.print(matrix[lowerI][j] + " ");
                lowerI++;
            }
            if(canContinue(lowerI, upperI, lowerJ, upperJ)){
                for(int i = lowerI; i <= upperI; i++)
                    System.out.print(matrix[i][upperJ] + " ");
                upperJ--;
            }
            if(canContinue(lowerI, upperI, lowerJ, upperJ)){
                for(int j = upperJ; j>= lowerJ; j--)
                    System.out.print(matrix[upperI][j] + " ");
                upperI--;
            }
            if(canContinue(lowerI, upperI, lowerJ, upperJ)){
                for(int i = upperI; i>= lowerI; i--)
                    System.out.print(matrix[i][lowerJ] + " ");
                lowerJ++;
            }
            if(!canContinue(lowerI, upperI, lowerJ, upperJ))
                break;
        }
        System.out.println();
    }

    private static boolean canContinue(int lowerI, int upperI, int lowerJ, int upperJ) {
        return lowerI <= upperI && lowerJ <= upperJ;
    }
}
