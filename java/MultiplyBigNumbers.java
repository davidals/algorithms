public class MultiplyBigNumbers {

    public static long multiplyOneDigit(String a, int digit){
        int result = 0;
        int multiplier = 1;
        char[] chars = a.toCharArray();
        for(int i = a.length() - 1; i >= 0; i--){
            result += Integer.parseInt(chars[i] + "") * digit * multiplier;
            multiplier *= 10;
        }
        return result;
    }
    public static long multiply(String a, String b){
        int multiplier = 1;
        int result = 0;

        char[] chars = b.toCharArray();
        for(int i = b.length() - 1; i >= 0; i--){
            int digit = Integer.parseInt(chars[i] + "");
            result += multiplyOneDigit(a,digit) * multiplier;
            multiplier *= 10;
        }
        return result;
    }
}
