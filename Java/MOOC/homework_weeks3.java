import java.util.Arrays;

public class homework_weeks3{
    public static void main(String[] args){

        // 初始化一个长度为101的布尔型数组，初始值都为true
        boolean[] isPrime = new boolean[101];
        Arrays.fill(isPrime, true);

        // 0和1不是素数，将其标记为false
        isPrime[0] = isPrime[1] = false;

        // 从2开始遍历到100
        for(int i = 2; i <= 100; i++){
            // 如果当前数字是素数
            if(isPrime[i]){
                // 将其倍数都标记为false
                for(int j = i * 2; j <= 100; j += i){
                    isPrime[j] = false;
                }
            }
        }
        
        // 输出所有素数
        int i = 0;
        for(boolean prime : isPrime){
            if(prime){
                System.out.print(i + " ");
            }
            i++;
        }
    }
}