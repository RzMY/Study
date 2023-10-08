public class PerfectNumber {
    public static void main(String[] args){
        for(int i = 1;i < 1000;i++){
            int sum = 0;
            int j = 1;
            while(i != j){
                if(i % j == 0){
                    sum += j;
                }
                j++;
            }
            if(sum == i){
                System.out.print(i + " ");
            }
        }
    }
}